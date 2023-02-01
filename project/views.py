from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project,Tag,Review
from .projectforms import Projectform,Reviewform
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utilities import project_search,project_pagination
# Create your views here.
def Projects(request):
    projectobj,search_query=project_search(request)
    custom,projectobj=project_pagination(request,projectobj,3)
    # custom=range(1,10)
    
    content={'projects':projectobj,'search_query':search_query,'custom':custom}
    return render(request,'projects/projects.html',content)

def single_project(request,pk):
    projectobj=Project.objects.get(id=pk)
            
    content={'project':projectobj}
    print(projectobj)
    return render(request,'projects/single_project.html',content)


def add_review(request,pk):
    projectobj=Project.objects.get(id=pk)
    form=Reviewform()
    if request.method=='POST':
        form=Reviewform(request.POST)
        if form.is_valid():
            review=form.save(commit=False)
            review.owner=request.user.profile
            review.project=projectobj
            review.save()
            print('review: ',review.id)
            print(review)
            projectobj.vote_cal
            messages.success(request,'Review added succesfully')
            
            return redirect('single_project' ,pk=projectobj.id)
            
    content={'project':projectobj,'forms':form}
    print(projectobj)
    return render(request,'projects/review_form.html',content)



def update_review(request,pk):
    # projectobj=Project.objects.get(id=pk)
    rev=Review.objects.get(id=pk)
    form=Reviewform(instance=rev)
    if request.method=='POST':
        form=Reviewform(request.POST,instance=rev)
        if form.is_valid():
            form.save()
            messages.success(request,'Review updated succesfully')
            return redirect(request.GET['next'] if request.GET['next'] else 'projects')
    content={'forms':form}
    return render(request,'projects/review_form.html',content)


def delete_review(request,pk):
    # projectobj=Project.objects.get(id=pk)
    rev=Review.objects.get(id=pk)
    form=Reviewform(instance=rev)
    if request.method=='POST':
       rev.delete()
       messages.success(request,'Review deleted succesfully')
       return redirect(request.GET['next'] if 'next' in request.GET['next'] else 'projects')
    content={'form':form}
    return render(request,'delete_project.html',content)




@login_required(login_url='login_page')
def create_project(request):
    profile=request.user.profile
    form=Projectform()
    
    if request.method=='POST':
        form=Projectform(request.POST,request.FILES)
        newtags=request.POST.get('newtags')
        if form.is_valid:
            project=form.save(commit=False)
            project.owner=profile
            project.save()
            newtags=newtags.replace(',',' ').split()
            for tag in newtags:
                print(tag)
                tag, created=Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('account')

    context={'forms':form,'project':form}
    return render(request,'projects/projectform.html',context)

@login_required(login_url='login_page')
def update_project(request,pk):
    profile=request.user.profile
    projectobj=profile.project_set.get(id=pk)
    # projectobj=Project.objects.get(id=pk)
    form=Projectform(instance=projectobj)
    newtags=request.POST.get('newtags')
    if request.method=='POST':
        
        # print(newtags)
        form=Projectform(request.POST,request.FILES,instance=projectobj)
       
        if form.is_valid:
            form.save()
            newtags=newtags.replace(',',' ').split()
            for tag in newtags:
                print(tag)
                tag, created=Tag.objects.get_or_create(name=tag)
                projectobj.tags.add(tag)
            return redirect('account')
    context={'forms':form,'project':projectobj}
    return render(request,'projects/projectform.html',context)

@login_required(login_url='login_page')
def delete_project(request,pk):
    profile=request.user.profile
    projectobj=profile.project_set.get(id=pk)
   
    # projectobj=Project.objects.get(id=pk)
    # form=Projectform(instance=projectobj)
    if request.method=='POST':
       projectobj.delete()
       return redirect('projects')
    context={'forms':projectobj}
    return render(request,'delete_project.html',context)

def vedio(request):
    project=Project.objects.all()
    content={'projects':project}
    return render(request,'projects/vedio.html',content)