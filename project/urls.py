from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
    path('',views.Projects,name='projects'),
    path('single_project/<str:pk>/',views.single_project,name='single_project'),
    # p ath('singleProject/<str:pk>/',views.new,name="single")
    path('create_project',views.create_project,name='create_project'),
    path('update_project/<str:pk>/',views.update_project,name='update_project'),
    path('delete_project/<str:pk>/',views.delete_project,name='delete_project'),
     path('add_review/<str:pk>/',views.add_review,name='add_review'),
    path('update_review/<str:pk>/',views.update_review,name='update_review'),
     path('delete_review/<str:pk>/',views.delete_review,name='delete_review'),
     path('vedio',views.vedio,name='vedios'),
    

    

]