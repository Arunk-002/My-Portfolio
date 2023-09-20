from django.shortcuts import render

# Create your views here.
def Gallery(request):
    return render(request,'photos/gallery.html') 
def viewPhoto(request, pk):
    return render(request,'photos/view_Photo.html') 
def addPhoto(request):
    return render(request,'photos/add.html') 
