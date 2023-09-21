from django.shortcuts import render
from photos.models import category,Photo
# Create your views here.
def Gallery(request):
    categories=category.objects.all()
    context={'categories': categories}
    return render(request,'photos/gallery.html',context) 
def viewPhoto(request, pk):
    return render(request,'photos/view_Photo.html') 
def addPhoto(request):
    return render(request,'photos/add.html') 
