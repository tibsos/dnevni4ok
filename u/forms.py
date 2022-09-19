from django import forms as f
from django.contrib.auth.forms import UserCreationForm as UCF
from django.contrib.auth.models import User as U

class RF(UCF):
    class Meta:
        model=U
        fields=('username','email','password1',)
        error_messages={
            'username':{
                "unique": "Дневничок с таким именем уже существует :c "
            },
            'email':{
                "invalid":"Пожалуйста, введи корректный почтовый адрес"
            }
        }
    def __init__(self,*args,**kwargs):
        super(RF,self).__init__(*args,**kwargs)
        del self.fields['password2']
        self.fields['password1'].help_text=None
        self.fields['username'].help_text=None