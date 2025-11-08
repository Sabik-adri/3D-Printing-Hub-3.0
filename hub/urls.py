from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book, name='book'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('table/', views.table, name='table'),
    path('contact/', views.contact, name='contact'),
    path('toggle-status/<int:client_id>/', views.toggle_status, name='toggle_status'),  # New URL
    
    path('plastic-service/', views.plastic_service, name='plastic_service'),
    path('plastic-service-sla/', views.plastic_service_sla, name='plastic_service_sla'),
    path('plastic-service-architectural/', views.plastic_service_architectural, name='plastic_service_architectural'),
    path('plastic-service-pcb/', views.plastic_service_pcb, name='plastic_service_pcb'),
    path('plastic-service-robotics/', views.plastic_service_robotics, name='plastic_service_robotics'),
    path('plastic-service-machine-spare-sparts/', views.plastic_service_machine_spare_sparts, name='plastic_service_machine_spare_sparts'),
    path('plastic-service-prosthetic/', views.plastic_service_prosthetic, name='plastic_service_prosthetic'),
    path('plastic-service-jig-and-fixture/', views.plastic_service_jig_and_fixture, name='plastic_service_jig_and_fixture'),
    path('plastic-service-custom/', views.plastic_service_Custom, name='plastic_service_Custom'),
    path('plastic-service-concept/', views.plastic_service_concept, name='plastic_service_concept'),

    
    path('create-blog/', views.create_blog, name='create_blog'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('how-it-works/', views.how_it_works, name='how_it_works'),
    path('design-guide/', views.design_guide, name='design_guide'),
    path('material-data-sheets/', views.material_data_sheets, name='material_data_sheets'),
    path('tolerance-and-accuracy', views.tolerance_and_accuracy, name='tolerance_and_accuracy'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)