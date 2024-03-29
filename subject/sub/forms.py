from django import forms
from .models import Subject


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"

        widgets = {
            "subject_name": forms.TextInput(attrs={'class': 'form-control'}),
            "subject_teacher": forms.TextInput(attrs={'class': 'form-control'}),
            "total_students": forms.NumberInput(attrs={'class': 'form-control'}),
            "subject_fee": forms.NumberInput(attrs={'class': 'form-control'}),
        }
