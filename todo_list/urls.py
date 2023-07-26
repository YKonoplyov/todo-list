from django.contrib import admin
from django.urls import path
from todo_list.views import (TaskListView, TagListView)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tag_list", TagListView.as_view(), name="tag-list"),
]

app_name = "todo_list"
