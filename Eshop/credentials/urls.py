from django.urls import path
from . import views
from django.urls import reverse

app_name = 'credentials'
urlpatterns = [

    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
