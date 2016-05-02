__author__ = 'viids'
from django import forms
from .models import SignUp

TOPIC_CHOICES = (
    ('general', 'General Enquiry'),
    ('bug', 'Bug Report'),
    ('Suggestion', 'Suggestion'),
)


class ContactForm(forms.Form):
    topic = forms.ChoiceField(choices=TOPIC_CHOICES)
    message = forms.CharField(widget=forms.Textarea())
    sender = forms.EmailField(required=False)


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['email', 'fullName']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extention = provider.split(".")
        if not extention == "edu":
            raise forms.ValidationError("Please Use Your .edu Email.")
        # if not domain == "csu":
        #     raise forms.ValidationError("Please Use Your CSU Email.")
        return email



