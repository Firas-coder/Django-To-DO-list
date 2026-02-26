from django import forms
from .models import ToDo
class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = '__all__'
        todo_status = [
    ('yes', 'Yes'),
    ('no', 'No'),
]
        labels = {
            'title': 'Title',
            'description': 'Description',
            'completed': 'Completed',
            'date_created': 'Date Created',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'completed': forms.Select(choices=todo_status),
        }   