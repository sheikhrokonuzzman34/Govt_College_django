from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    institution_info = Institution_info.objects.all()
    
    context ={
            'institution_info':institution_info
        }
    
    return render(request, 'main_app/index.html', context)

def classRoutine(request):
    return render(request, 'main_app/classRoutine.html')

def notices(request):
    notice = Notice.objects.all().order_by("-id")
    
    context = {
        'notice': notice
        }
    return render(request, 'main_app/notices.html',context)

def managing_committee(request):
    managing = Managing_committee.objects.all().exclude(ordering=1)
    head = Managing_committee.objects.get(ordering=1)
    
    context = {
        'managing': managing,
        'head': head
        }
    return render(request, 'main_app/managing_committee.html',context)



def photoGallery(request):
    photo_g = Photo_gallery.objects.all()
    context={
        'photo_g':photo_g
    }
    return render(request, 'main_app/photoGallery.html',context)

    

def video_gallery(request):
    video_g = Video_gallery.objects.all()
    context={
        'video_g':video_g
    }
    return render(request, 'main_app/videoGallery.html',context)