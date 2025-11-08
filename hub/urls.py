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

    
    path('create-blog/', views.create_blog, name='create_blog'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)