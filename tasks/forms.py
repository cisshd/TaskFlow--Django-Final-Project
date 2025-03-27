from django import forms
from .models import Task
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'status', 'assigned_to']

    assigned_to = forms.ModelChoiceField(queryset=User.objects.all(), required=False, empty_label="Assign to")
