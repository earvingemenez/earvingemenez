from django import forms
from .models import Message


class ContactForm(forms.ModelForm):

    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'You wanna talk about...',
            }
    ))

    class Meta:
        model = Message
        fields = ['name', 'email', 'content']