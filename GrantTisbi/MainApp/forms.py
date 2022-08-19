from django import forms
from .models import FeedBack
from django.core.exceptions import ValidationError

class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ['FIO', 'email', 'text']

        widgets = {
            'FIO': forms.TextInput(attrs={
                'class': 'form-input',

            }),
            'email': forms.TextInput(attrs={
                'class': 'form-input',

            }),
            'text': forms.Textarea(attrs={
                'class': 'form-text',

            }),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if "@" not in email:
            raise ValidationError("Некорректный ввод")
        return email