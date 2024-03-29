from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
       path('', views.IndexView.as_view(), name='index'),
       path('delete/<int:todo_id>', views.complete_todo, name="delete")
]