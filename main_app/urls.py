from django.urls import path
from .views import * 



urlpatterns = [
     path('',index ,name='index'),
     path('classRoutine/',classRoutine ,name='classRoutine'),
     path('notices/',notices ,name='notices'),
     path('managing_committee/',managing_committee ,name='managing_committee'),
     path('photoGallery/',photoGallery ,name='photoGallery'),
     path('video_gallery/',video_gallery ,name='video_gallery'),
]