
from django.urls import path
from . import views

urlpatterns = [
    path('home_register',views.home_register, name='home_register'),
#    path('register_home',views.register_home, name='register_home'),
    path('logout',views.logout, name='logout'),
    path('register',views.register, name='register'),
    path('login',views.login, name='login'),
]
