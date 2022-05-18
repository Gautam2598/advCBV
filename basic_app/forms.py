from dataclasses import field
from django import forms

from basic_app.models import Company


class CompanyAddForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"
        

