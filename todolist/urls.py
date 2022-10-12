from django.urls import path
from todolist.views import TodolistsDataView, create_task, post_todolist, register, show_ajax_todolist
from todolist.views import login_user
from todolist.views import logout_user 
from todolist.views import show_todolist 
from todolist.views import show_json

app_name = 'todolist'
urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('ajax/', show_ajax_todolist, name='show_ajax_todolist'),
    path('ajax/data', TodolistsDataView.as_view(), name='todolist_data'),
    path('add/', post_todolist, name='post_todolist'),
    path('json/', show_json, name='show_json'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task')
]