from django import forms
from .models import Task, Tag
from django.forms import DateInput


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Task
        fields = ['content', 'deadline', 'is_done', 'tags']
        widgets = {
            'deadline': DateInput(attrs={'type': 'date', 'placeholder': 'DD/MM/YYYY'}, format='%d/%m/%Y'),
        }

    def clean_deadline(self):
        deadline = self.cleaned_data.get('deadline')
        return deadline
