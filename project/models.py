from django.db import models
from users.models import Profile
import uuid
from datetime import datetime
# Create your models here.
class Project(models.Model):
    owner=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=30)
    description=models.TextField(max_length=300,blank=True,null=True)
    website_link=models.CharField(max_length=100,blank=True,null=True)
    manga_link=models.CharField(max_length=100,blank=True,null=True)
    project_image=models.ImageField(default='default.jpg',blank=True,null=True)
    vedio=models.FileField(blank=True,null=True,upload_to='images/vedio')
    tags=models.ManyToManyField('Tag',blank=True)
    vote_total=models.IntegerField(default=0,blank=True,null=True)
    vote_ratio=models.IntegerField(default=0,blank=True,null=True)
    created=models.DateTimeField(default=datetime.now())
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['-vote_ratio','-vote_total','title']

    @property
    def single_review(self):
        reviewers=self.review_set.all().values_list('owner__id',flat=True)
        return reviewers


    @property
    def vote_cal(self):
        reviews=self.review_set.all()
        up_vote=reviews.filter(value='Up').count()
        vote_total=reviews.count()
        ratio=(up_vote/vote_total)*100
        self.vote_total=vote_total
        self.vote_ratio=ratio
        self.save()

    @property
    def image_url(self):
        try:
            url=self.project_image.url
        except:
            url=''
        return url

class Review(models.Model):
    Vote_type=(
         ('Up',"up_vote"),
          ('down',"down_vote"),
    )
    owner=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    body=models.TextField(blank=True,null=True)
    value=models.CharField(max_length=10,choices=Vote_type)
    created=models.DateTimeField(default=datetime.now())
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self):
        return self.value

    class Meta:
        unique_together=[['owner','project']]
    



class Tag(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    created=models.DateTimeField(default=datetime.now())
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self):
        return self.name