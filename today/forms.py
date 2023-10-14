from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django import forms
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ["first_name","last_name","email","username","password1","password2"]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        dic = {
            "first_name":"First Name",
            "last_name":"Last Name",
            "email":"Email",
            "username":"Username",
            "password1":"Password",
            "password2":"Confirm Password"}
        for i in self.fields:
            self.fields[i].widget.attrs['class']='form-control'
            self.fields[i].widget.attrs['placeholder']= dic[i]
            self.fields[i].label = dic[i]

class ProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ["first_name","last_name","username","email"]
    
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        dic = {
            "first_name":"First Name",
            "last_name":"Last Name",
            "email":"Email",
            "username":"Username",
            "password1":"Password",
            "password2":"Confirm Password"}
        for i in self.fields:
            self.fields[i].widget.attrs['class']='form-control'
            self.fields[i].widget.attrs['placeholder']= self.fields[i].label
            
          
class ResetPasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ["old_password","new_password1","new_password2"]
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        dic = {
            "old_password":"Old password",
            "new_password1":"New password",
            "new_password2":"Confirm password"}
        for i in self.fields:
            self.fields[i].widget.attrs['class']='form-control'
            self.fields[i].widget.attrs['placeholder']= dic[i]
            self.fields[i].label = dic[i]