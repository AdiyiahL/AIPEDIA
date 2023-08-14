from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('choose_login/', views.choose_login, name='choose_login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('success_signup/', views.success_signup, name='success_signup'),
    path('profile/', views.profile, name='profile'),
    ]