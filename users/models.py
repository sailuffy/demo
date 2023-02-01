from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save,post_delete
from datetime import datetime
# Create your models here.
class Profile(models.Model):
  user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
  name=models.CharField(max_length=50,null=True,blank=True)
  short_intro=models.TextField(null=True,blank=True)
  bio=models.TextField(null=True,blank=True)
  username=models.CharField(max_length=50,null=True,blank=True)
  email=models.CharField(max_length=50,null=True,blank=True)
  insta_id=models.CharField(max_length=50,null=True,blank=True)
  profile_pic=models.ImageField(blank=True,null=True,upload_to='profile/',default='profile/user-default.png')
  location=models.CharField(max_length=50,null=True,blank=True)
  github_link=models.CharField(max_length=100,null=True,blank=True)
  twitter_acc=models.CharField(max_length=50,null=True,blank=True)
  Linkedin=models.CharField(max_length=50,null=True,blank=True)
  youtube_acc=models.CharField(max_length=150,null=True,blank=True)
  created=models.DateTimeField(default=datetime.now())
  id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)


  def __str__(self):
    return str(self.user.username)
  
  class Meta:
    ordering=['created']

  @property
  def image_url(self):
      try:
          url=self.profile_pic.url
      except:
          url=''
      return url



class Skills(models.Model):
  profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
  name=models.CharField(max_length=50,null=True,blank=True)
  description=models.TextField(null=True,blank=True)
  created=models.DateTimeField(default=datetime.now())
  id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

  def __str__(self):
    return self.name


class Message(models.Model):
  sender=models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,blank=True)
  reciver=models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,blank=True,related_name="messages")
  name=models.CharField(max_length=50,null=True,blank=True)
  email=models.EmailField(max_length=50,null=True,blank=True)
  subject=models.CharField(max_length=100,null=True,blank=True)
  body=models.TextField()
  unread_msgs=models.BooleanField(default=False,null=True)
  created=models.DateTimeField(default=datetime.now())
  id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

  def __str__(self):
    return self.name
  class Meta:
    ordering=['unread_msgs','-created']



