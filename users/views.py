from django.shortcuts import render,redirect
from .models import Profile,Skills,Message
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .userforms import registerform,Profileform,Skillsform,Messageform
from .utilities import search_user,profile_pagination
# Create your views here.
def profile(request):
    profile,search_query=search_user(request)
    custom,profile=profile_pagination(request,profile,3)
    content={'profiles':profile,'search_query':search_query,'custom':custom}
    return render(request,'users/profile.html',content)

def single_profile(request,pk):
    profile=Profile.objects.get(id=pk)
    topskills=profile.skills_set.exclude(description__iexact="")
    otherskills=profile.skills_set.filter(description__iexact="")
    content={'profiles':profile,'topskills':topskills,'otherskills':otherskills}
    return render(request,'users/single_user.html',content)


def loginpage(request):
    page='login'
    context={'page':page}
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method=='POST':
        username=request.POST['username'].lower()
        password=request.POST['password']
        # print(username,password)
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,"user not found")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            messages.success(request,"login success")
            login(request,user)
            return redirect('account')
        else:
           messages.error(request,"invalid passwrd/mail")
        
    return render(request,'users/login_register.html',context)

def logoutpage(request):
    page='login'
    context={'page':page}
    messages.success(request,"logout sucessfully")
    logout(request)
    return redirect('login_page')

def registerpage(request):
    page='register'
    form=registerform()
    if request.method=='POST':
        form=registerform(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            print(user)
            user.username=user.username.lower()
            user.save()
            messages.success(request,"acc created succesfully")
            login(request,user)
            return redirect('account')   
        else:
             messages.error(request,"somethng went wrng")


    context={'page':page,'form':form}
    return render(request,'users/login_register.html',context)

@login_required(login_url='login_page')
def account(request):
    profile=request.user.profile
    skills=profile.skills_set.all()
    projects=profile.project_set.all()
    content={'profile':profile,'skills':skills,'projects':projects}

    return render(request,'users/account.html',content)

@login_required(login_url='login_page')
def edit_profile(request):
    profile=request.user.profile
    form=Profileform(instance=profile)
    if request.method=='POST':
        form=Profileform(request.POST,request.FILES ,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
    content={'form':form}
    return render(request,'users/edit-profile.html',content)


@login_required(login_url='login_page')
def create_skill_profile(request):
    profile=request.user.profile
    form=Skillsform()
    if request.method=='POST':
        form=Skillsform(request.POST)
        if form.is_valid():
            skills=form.save(commit=False)
            skills.profile=profile
            skills.save()
            messages.success(request,"Skill was added successfully")
            return redirect('account')
    content={'form':form}
    return render(request,'users/skill_profile.html',content)


@login_required(login_url='login_page')
def update_skill_profile(request,pk):
    profile=request.user.profile
    skill=profile.skills_set.get(id=pk)
    form=Skillsform(instance=skill)
    if request.method=='POST':
        form=Skillsform(request.POST,instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request,"Skill was updated successfully")
            return redirect('account')
    content={'form':form}
    return render(request,'users/skill_profile.html',content)


@login_required(login_url='login_page')
def delete_skill_profile(request,pk):
    profile=request.user.profile
    skill=profile.skills_set.get(id=pk)
    form=Skillsform(instance=skill)
    if request.method=='POST':
        form=Skillsform(request.POST,instance=skill)
        if form.is_valid():
            form.delete()
            messages.success(request,"Skill was deleted successfully")
            return redirect('account')

    content={'form':form}
    return render(request,'delete_project.html',content)


@login_required(login_url='login_page')
def inbox_messages(request):
    profile=request.user.profile
    messagereq=profile.messages.all()
    unread=profile.messages.filter(unread_msgs=False).count()
    context={'messageRequests':messagereq,'unread':unread}
    return render(request,'users/inbox.html',context)

@login_required(login_url='login_page')
def message_body(request,pk):
    profile=request.user.profile
    messagereq=profile.messages.get(id=pk)
    print(messagereq.unread_msgs)
    if not messagereq.unread_msgs:
        messagereq.unread_msgs=True
        messagereq.save()
    context={'message':messagereq}
    return render(request,'users/message.html',context)


def send_messages(request,pk):
    receiver=Profile.objects.get(id=pk)
    form=Messageform()

    try:
        sender=request.user.profile
    except:
        sender=None
    if request.method=='POST':
        form=Messageform(request.POST)
        if form.is_valid():
            msg=form.save(commit=False)
            msg.sender=sender
            msg.reciver=receiver
            
            if sender:
                msg.name=sender.name
            msg.save()
            messages.success(request,'message sent succesfuully')
            return redirect('single_profile',pk=receiver.id)
    content={'form':form,'receiver':receiver}
    return render(request,'users/message_form.html',content)