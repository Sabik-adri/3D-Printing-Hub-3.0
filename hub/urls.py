from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book, name='book'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('table/', views.table, name='table'),
    path('contact/', views.contact, name='contact'),
    path('toggle-status/<int:client_id>/', views.toggle_status, name='toggle_status'),  # New URL
]