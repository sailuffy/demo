from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save,post_delete
from .models import Profile,Message
from django.conf import settings
from django.core.mail import send_mail

def create_profile(sender,instance,created,**kwargs):

  if created:
    user=instance
    profile=Profile.objects.create(
      user=user,
      username=user.username,
      email=user.email,
      name=user.first_name
    )
    subject="Welcome to Sai lokesh website"
    message=f"Thank u {user.username} for registering ur account. We extend our warmest greeting to you! You are an excellent addition to my website"
    

    send_mail(
      subject,
      message,
      settings.EMAIL_HOST_USER,
      [profile.email],
      fail_silently=False,
    )


post_save.connect(create_profile,sender=User)



def delete_user(sender,instance,**kwargs):
  try:
    user=instance.user
    print(user.id)
    print(user.username)
    user.delete()
  except:
    pass
post_delete.connect(delete_user,sender=Profile)



def update_profile(sender,instance,created,**kwargs):

  if not created:
    profile=instance
    user=profile.user
    user.username=profile.username
    user.email=profile.email
    user.save()
    
post_save.connect(update_profile,sender=Profile)


def messagee_sent(sender,instance,created,**kwargs):
  if created:
    owner=Profile.objects.get(name__icontains='sai lokesh')
    print('ur answer',owner)
    user=instance
    message=Message.objects.create(
      reciver=user,
      subject="Thanks for registering",
      sender=owner,
      body=f"hi  {user.username} thank u for joining.. explore the things",
      name='sai'
    )

post_save.connect(messagee_sent,sender=Profile)