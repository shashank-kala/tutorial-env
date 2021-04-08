from django.urls import path
from . import views

urlpatterns = [
path('',views.index,name ="List"),
path('Update_Task/<str:pk>/', views.updateTask, name="Update_Task"),
path('Delete_Task/<str:pk>/', views.deleteTask, name="Delete_Task")
]