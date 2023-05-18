from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from todoapp import views
from todoproject import settings

urlpatterns = [

    path('', views.add, name='add'),
    # path('details/', views.details, name="details"),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    #path('cbvhome/', views.TaskListView.as_view, name='cbvhome'),
    #path('cbvdetail/<int:pk>/', views.TaskDetailView.as_view(), name='cbvdetail'),
   # path('cbvupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='cbvupdate'),

]
