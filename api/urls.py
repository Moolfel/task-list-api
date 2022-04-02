from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [
    path('', views.api_overview, name="api_overview"),
    path('task-list/', views.task_list, name="task-list"),
    path('task-detail/<pk>/', views.task_detail, name="task-detail"),
     
    path('task-create/', views.task_create, name="task-create"),
    path('task-update/<pk>/', views.task_update, name="task-update"),
    path('task-delete/<pk>/', views.task_delete, name="task-delete"),

]
