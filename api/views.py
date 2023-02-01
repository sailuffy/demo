from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import Projectserializer,Reviewserializer
from project.models import Project,Review,Tag


@api_view(['GET'])
def getRoutes(request):
    routes=[
        {'GET' :'/api/projects'},
        {'GET' :'/api/projects/id'},
        {'POST' :'/api/projects/id/vote'},
        {'POST' :'/api/users/token'},
       {'POST' :'/api/users/token/refresh'},
  
    ]
    return Response(routes)

@api_view(['GET'])
def getProjects(request):
    projects=Project.objects.all()
    serialize=Projectserializer(projects,many=True)
    return Response(serialize.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProject(request,pk):
    projects=Project.objects.get(id=pk)
    serialize=Projectserializer(projects,many=False)
    return Response(serialize.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectvote(request,pk):
    project=Project.objects.get(id=pk)
    data=request.data
    print(data)
    user=request.user.profile
    review,created=Review.objects.get_or_create(
        project=project,
        owner=user,
    )
    review.value=data['value']
    review.save()
    project.vote_cal
    serializer=Projectserializer(project,many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def remove_tag(request):
    projectid=request.data['project']
    tagid=request.data['tag']
    project=Project.objects.get(id=projectid)
    tag=Tag.objects.get(id=tagid)
    project.tags.remove(tag)
    return Response('tag was removed!!')