from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Blog, Client
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Employee
from .forms import EmployeeForm

def home(request):
    employees = Employee.objects.all()

    # Group employees into chunks of 3
    def chunked(qs, n):
        for i in range(0, len(qs), n):
            yield qs[i:i+n]

    employee_groups = list(chunked(list(employees), 3))

    return render(request, 'index.html', {'employee_groups': employee_groups})

def book(request):
    if request.method == 'POST':
        Client.objects.create(
            name=request.POST['name'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            message=request.POST['message'],
            date=request.POST['date'],
            time=request.POST['time']
        )
        return redirect('home')
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('table')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def table(request):
    clients = Client.objects.all().order_by('-id')
    return render(request, 'table.html', {'data': clients})

def contact(request):
    if request.method == 'POST':
        Client.objects.create(
            name=request.POST['name'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            message=request.POST['message'],
            date=request.POST['date'],
            time=request.POST['time']
        )
        return redirect('contact')
    return render(request, 'contact.html')



@login_required
def toggle_status(request, client_id):
    if request.method == 'POST':
        try:
            client = Client.objects.get(id=client_id)
            client.is_done = not client.is_done  # Toggle status
            client.save()
            return JsonResponse({'success': True, 'is_done': client.is_done})
        except Client.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Client not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request'})

def plastic_service(request):
    return render(request, 'service-single.html')

def plastic_service_sla(request):
    return render(request, 'service-single-sla.html')

def plastic_service_architectural(request):
    return render(request, 'service-single-architectural.html')

def plastic_service_pcb(request):
    return render(request, 'service-single-pcb.html')

def plastic_service_robotics(request):
    return render(request, 'service-single-robotics.html')

def plastic_service_machine_spare_sparts(request):
    return render(request, 'service-single-machine-spare-parts.html')

def plastic_service_prosthetic(request):
    return render(request, 'service-single-prosthetic.html')

def plastic_service_jig_and_fixture(request):
    return render(request, 'service-single-jig-and-fixture.html')

def plastic_service_Custom(request):
    return render(request, 'service-single-custom.html')

def plastic_service_concept(request):
    return render(request, 'service-single-concept.html')


def create_blog(request):
    if request.method == 'POST':
        try:
            blog = Blog.objects.create(
                title=request.POST['title'],
                content=request.POST['content'],
                image=request.FILES['image'],
                date=request.POST['date'],
                time=request.POST['time'],
                created_by=request.user
            )
            return redirect('blog', blog.id)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return render(request, 'create_blog.html')


def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog_detail.html', {'blog': blog})


def how_it_works(request):
    return render(request, 'how_it_works.html')

def design_guide(request):
    return render(request, 'design_guide.html')

def material_data_sheets(request):
    return render(request, 'material_data_sheets.html')

def tolerance_and_accuracy(request):
    return render(request, 'tolerance_and_accuracy.html')



def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})

def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('employee_list')
