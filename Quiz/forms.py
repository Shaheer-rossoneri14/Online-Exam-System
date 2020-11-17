from django.contrib.auth.models import User
from django import forms

class Registration(forms.ModelForm):
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Firstrname'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Lastname'}))
    password = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
    email = forms.CharField(max_length=50,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}))
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password','email']

    def clean_username(self):
        user = self.cleaned_data['username']
        try:
            match = User.objects.get(username=user)
        except:
            return self.cleaned_data['username']
        raise forms.ValidationError("This Username is already exist Please try another")

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            match = User.objects.get(email=email)
        except:
            return self.cleaned_data['email']
        raise forms.ValidationError("This Email already exist Please try another")

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password)<8:
            raise forms.ValidationError("Password length should be minimum 8 character")
        if password.isdigit():
            raise forms.ValidationError("Password should be alphanumeric")
        else:
            return self.cleaned_data['password']