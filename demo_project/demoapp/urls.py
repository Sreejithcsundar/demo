from django.urls import path

from demoapp import views
app_name = 'demoapp'
urlpatterns = [

    path('', views.home, name='home')
]
