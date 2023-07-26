from django.contrib import admin
from django.urls import path
from todo_list.views import (TaskListView, TagListView, TagCreateView)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tag_list", TagListView.as_view(), name="tag-list"),
    path("tag_list/create", TagCreateView.as_view(), name="tag-create"),
]

app_name = "todo_list"
