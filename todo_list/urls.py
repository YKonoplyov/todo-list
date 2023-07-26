from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.urls import path
from todo_list.views import (TaskListView, TagListView, TagCreateView,
                             TagUpdateView, TagDeleteView, TaskCreateView,
                             TaskUpdateView, TaskDeleteView,
                             change_task_statement, UserCreateView)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task_create", TaskCreateView.as_view(), name="task-create"),
    path(
        "task_update/<int:pk>/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "task_delete/<int:pk>/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "task_change_state/<int:task_id>/",
        change_task_statement,
        name="task-change"
    ),
    path("tag_list", TagListView.as_view(), name="tag-list"),
    path("tag_list/create", TagCreateView.as_view(), name="tag-create"),
    path(
        "tag_list/update/<int:pk>",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
            "tag_list/<int:pk>/delete",
            TagDeleteView.as_view(),
            name="tag-delete"
        ),
    path("register/", UserCreateView.as_view(), name="register")
]

app_name = "todo_list"
