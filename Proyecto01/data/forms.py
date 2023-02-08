from django import forms
from data.models import IndexChange

class IndexChangeForm(forms.ModelForm):
    class Meta:
        model = IndexChange
        fields = '__all__'