from django import forms
from todo_list.models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = "__all__"
