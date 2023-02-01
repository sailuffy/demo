from django.db import models
from django.forms import ModelForm,widgets
from .models import Project,Review
from  django import forms
from django.contrib.auth.forms import UserCreationForm

class Projectform(ModelForm):
    class Meta:
        model =Project
        fields=['title','description','website_link','manga_link','project_image','vedio']
        labels={'project_image':'Anime_image'}
        widgets={
            'tags':forms.CheckboxSelectMultiple()
        }

    def __init__(self,*args,**kwargs):
        super(Projectform,self).__init__(*args,**kwargs)
       

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class Reviewform(ModelForm):
    class Meta:
        model=Review
        fields=['value','body']
        labels= {
            'value':'place your vote',
            'body':'add a comment on the project'
        }
    
    def __init__(self,*args,**kwargs):
        super(Reviewform,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})