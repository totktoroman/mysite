from django import forms
from .models import *

class AddGroupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group_title'].empty_label = "Категория не выбрана"

    class Meta:
        model = Group
        fields = ['group_number', 'group_title']
        widgets = {
            'group_number': forms.TextInput(attrs={'class': 'form-input'}),


        }
