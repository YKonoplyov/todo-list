from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from todo_list.forms import TaskForm, UserForm
from todo_list.models import Task, Tag


class UserCreateView(generic.CreateView):
    model = get_user_model()
    form_class = UserForm


class TaskListView(generic.ListView):
    model = Task

    paginate_by = 5

    def get_queryset(self):
        self.queryset = Task.objects.filter(user__id=self.request.user.id)
        return self.queryset


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_list:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_list:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:task-list")


class TagListView(generic.ListView):
    model = Tag

    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list:tag-list")


def change_task_statement(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = not task.is_completed

    task.save()
    return redirect(reverse_lazy("todo_list:task-list"))