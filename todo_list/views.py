from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from todo_list.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagDeleteForm(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list:tag-list")
