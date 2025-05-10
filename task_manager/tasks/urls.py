from django.contrib import admin
from django.urls import path
from .views import create_view,update_view,delete_view,task_list_view,task_detail_view,index

urlpatterns = [
    path('',index,name='index'),
    path('create_view/',create_view,name='create_view'),
    path('update_view/<int:id>',update_view,name='update_view'),
    path('delete_view/<int:id>',delete_view,name='delete_view'),
    path('task_list_view/',task_list_view,name='task_list_view'),
    path('task_detail_view/<int:id>',task_detail_view,name='task_detail_view')
]
