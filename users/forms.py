from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User

from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


            
class ResetForm(PasswordResetForm):
    email = forms.EmailField()    
    fields = ['email']
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 

        self.fields['email'].label=""
      
        self.fields['email'].widget.attrs.update({ 
            'class': 'form-control', 
            'required':'', 
            'type':'email', 
            'placeholder':'Email',
            }) 


