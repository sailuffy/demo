from .models import Project,Tag,Review
from django.db.models import Q
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage

def project_search(request):
    search_query=""
    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')
    tag=Tag.objects.filter(name__icontains=search_query)
    projectobj=Project.objects.distinct().filter(Q(title__icontains=search_query)
    |Q(description__icontains=search_query)
    |Q(owner__name__icontains=search_query)
    |Q(tags__in=tag))

    return projectobj,search_query

def project_pagination(request,projectobj,res):
    page=request.GET.get('page')
    p=Paginator(projectobj,res)
    try:
        projectobj=p.page(page)
    except PageNotAnInteger:
        page=1
        projectobj=p.page(page)
    except EmptyPage:
        page=p.num_pages
        projectobj=p.page(page)

    left_index=int(page)-3
    if left_index<1:
        left_index=1
    right_index=int(page)+4
    if right_index>p.num_pages:
        right_index=p.num_pages+1
    custom=range(left_index,right_index)
    return custom,projectobj