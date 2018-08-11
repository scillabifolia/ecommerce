from django import forms
from django.contrib.auth import get_user_model
#from django.core.mail import send_mail

User = get_user_model()

#in clasa asta definesc 3 fielduri

class ContactForm(forms.Form):
    full_name = forms.CharField(
           widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Hi there!",
                    'id': "form_full_name"
                }
                )
           )
    email = forms.EmailField(widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your email",
                    'id': "form_full_name"
                }
                )
           )
    content = forms.CharField(
            max_length= 300,
            #help_text='100 characters max.',
            widget=forms.Textarea(
                  attrs={
                        'class': 'form-control',
                        'placeholder': 'Your full message'
                }
                )
            )

    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     if "gmail.com" not in email:
    #         raise forms.ValidationError("Email has to be gmail.com")
    #     return email


class LoginForm(forms.Form):
    username = forms.CharField(
           widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Hi there!",
                    'id': "form_username"
                }
                )
           )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your password",
                'id': "form_full_name"
                }
                )
            )


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Hi there!",
                'id': "form_username"
                }
                )
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your email",
                'id': "form_full_name"
                }
                )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your password",
                'id': "form_full_name"
                }
                )
    )

    password_confirmation = forms.CharField(
        label='Confirm password',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password confirmation",
                'id': "form_full_name"
                }
                )
    )
    #validation rule for new users not to be able to choose same email as others/ if a new user is created this function let's you get away with it
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs =User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs =User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if password_confirmation != password:
            raise forms.ValidationError("Passwords must match.")
        return data



