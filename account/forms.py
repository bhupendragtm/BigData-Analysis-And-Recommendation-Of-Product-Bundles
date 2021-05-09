from django import forms
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserCreationForm(forms.ModelForm):
    first_name = forms.CharField(widget= forms.TextInput,label="Firstname:")
    last_name= forms.CharField(widget=forms.TextInput,label="Lastname:")
    #username = forms.CharField(widget = forms.TextInput,label = "Username:")
    email = forms.EmailField(widget=forms.EmailInput,label = "Email:")
    password1 = forms.CharField(widget=forms.PasswordInput,label="Password:")
    password2 = forms.CharField(widget=forms.PasswordInput,label="Confirm Password:")

    # username.widget.attrs.update({
    #     "placeholder":"Enter Username"
    # })

    first_name.widget.attrs.update({
        "placeholder":"Enter FirstName"
    })
    last_name.widget.attrs.update({
        "placeholder":"Enter LastName"
    })
    email.widget.attrs.update({
        "placeholder":"Enter Email ID"
    })
    password1.widget.attrs.update({
        "placeholder":"Enter Password"
    })
    password2.widget.attrs.update({
        "placeholder":"Enter Password Again"
    })


    def clean(self):
        cleaned_data = super().clean()
        emailid = cleaned_data["email"]
        password = cleaned_data["password1"]
        repassword = cleaned_data["password2"]

        if(password != repassword):
            self.add_error('password2',"Passwords you entered don't match.")

        if(User.objects.filter(email = emailid).exists()):
            self.add_error('email',"A user with that email already exists.")
        

    class Meta:
        model = User
        fields = ['first_name','last_name','email','password1','password2']


class UserLoginForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput,label="Email:")
    password = forms.CharField(widget=forms.PasswordInput,label="Password:")
    email.widget.attrs.update({
        "placeholder":"Enter Email ID"
    })

    password.widget.attrs.update({
        "placeholder":"Enter Password"
    })

    def clean(self):
        cleaned_data = super().clean()
        emailid = cleaned_data['email']
        password = cleaned_data['password']
        user = authenticate(
            username = emailid,
            password = password
        )
        if user is None:
            raise ValidationError("Username or password you entered don't match.")

    
    class Meta:
        model = User
        fields = ['email','password']