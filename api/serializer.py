from rest_framework import serializers
from project.models import Project,Review,Tag
from users.models import Profile


class Reviewserializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields="__all__"


class Profileserializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields="__all__"



class Tagserializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields="__all__"



class Projectserializer(serializers.ModelSerializer):
    owner=Profileserializer(many=False)
    tags=Tagserializer(many=True)
    class Meta:
        model=Project
        fields="__all__"