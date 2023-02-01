from .models import Profile,Skills
from django.db.models import Q
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage


def search_user(request):
    search_query=""
    if request.GET.get('search_query'):
        print(request.GET.get('search_query'))
        search_query=request.GET.get('search_query')
    skills=Skills.objects.filter(name__icontains=search_query)
    profile=Profile.objects.distinct().filter(Q(name__icontains=search_query) |Q(insta_id__icontains=search_query)
    |Q(skills__in=skills))

    return profile,search_query



def profile_pagination(request,profile,res):
    page=request.GET.get('page')
    p=Paginator(profile,res)
    try:
        profile=p.page(page)
    except PageNotAnInteger:
        page=1
        profile=p.page(page)
    except EmptyPage:
        page=p.num_pages
        profile=p.page(page)

    left_index=int(page)-3
    if left_index<1:
        left_index=1
    right_index=int(page)+4
    if right_index>p.num_pages:
        right_index=p.num_pages+1
    custom=range(left_index,right_index)
    return custom,profile