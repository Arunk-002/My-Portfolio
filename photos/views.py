from django.shortcuts import render
from photos.models import category,Photo
# Create your views here.
def Gallery(request):
    categories=category.objects.all()
    photos=Photo.objects.all()
    context={'categories': categories,'photos':photos}
    return render(request,'photos/gallery.html',context) 

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    context={'photo':photo}
    return render(request,'photos/view_photo.html',context) 

def addPhoto(request):
    return render(request,'photos/add.html') 
