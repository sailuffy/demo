from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from  .models import Profile,Skills,Message

    
class registerform(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','email','username','password1','password2']

    def __init__(self,*args,**kwargs):
        super(registerform,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class Profileform(ModelForm):
    class Meta:
        model=Profile
        fields=['name','short_intro','bio','username','email','insta_id','profile_pic','location','github_link','twitter_acc','Linkedin','youtube_acc']
        labels={'bio':'About Me/Bio'}
    def __init__(self,*args,**kwargs):
        super(Profileform,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class Skillsform(ModelForm):
    class Meta:
        model=Skills
        fields='__all__'
        exclude=['profile']
    def __init__(self,*args,**kwargs):
        super(Skillsform,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class Messageform(ModelForm):
    class Meta:
        model=Message
        fields='__all__'
        exclude=['sender','reciver','unread_msgs']
    def __init__(self,*args,**kwargs):
        super(Messageform,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
