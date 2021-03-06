from django.urls import path

from App import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_task/<str:pk>/', views.updateTask, name='update'),
    path('delete/<str:pk>/', views.deleteTask, name='delete'),
]