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
    
    path('create-blog/', views.create_blog, name='create_blog'),
    path('blog/', views.blog, name='blog'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)