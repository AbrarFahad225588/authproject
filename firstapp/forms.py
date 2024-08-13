from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm,self).__init__(*args, **kwargs)
        fields=['username','first_name','last_name','email','password1','password2']
        for field in fields :
            self.fields[field].help_text=None
            self.fields[field].widget.attrs.update({'class':'form-control'})
        
    class Meta:
        model = User
        fields=['username','first_name','last_name','email']