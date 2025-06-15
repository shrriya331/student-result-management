from django import forms
from .models import Marks

class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['student', 'subject', 'marks_obtained', 'max_marks']
