from django.contrib import admin
from django.urls import path ,include
from todo_api import urls as todo_urls
from todo_api import views 
from django.urls import path, include
from .views import (
    TodoListApiView,

TodoDetailApiView
)


urlpatterns = [
    path('api/', TodoListApiView.as_view()),
    path('api/<int:todo_id>/', TodoDetailApiView.as_view()),

]