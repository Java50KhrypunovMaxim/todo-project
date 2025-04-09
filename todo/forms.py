from django import forms
from .models import Tag

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Task
        fields = ['content', 'deadline', 'is_done', 'tags']