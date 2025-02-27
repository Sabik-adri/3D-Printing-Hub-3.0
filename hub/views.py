from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Client
from django.http import JsonResponse

def home(request):
    return render(request, 'index.html')

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