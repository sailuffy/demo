from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
path('',views.profile,name='profile'),
path('single_profile/<str:pk>/',views.single_profile,name='single_profile'),
path('login_page',views.loginpage,name='login_page'),
path('logout_page',views.logoutpage,name='logout_page'),
path('register',views.registerpage,name='register'),
path('account',views.account,name='account'),
path('edit_profile',views.edit_profile,name='edit_profile'),
path('skill_profile',views.create_skill_profile,name='skills_profile'),
path('update_skill_profile/<str:pk>/',views.update_skill_profile,name='update_skill_profile'),
path('delete_skill_profile/<str:pk>/',views.delete_skill_profile,name='delete_skill_profile'),
path('inbox_msgs',views.inbox_messages,name='inbox_msgs'),
path('msgs/<str:pk>/',views.message_body,name='messages'),
path('send_msgs/<str:pk>/',views.send_messages,name='send_messages'),
]