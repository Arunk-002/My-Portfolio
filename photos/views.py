from django.shortcuts import render,redirect
from django.contrib import messages
from photos.models import Category,Photo
# Create your views here.
def Gallery(request):
    categories=Category.objects.all()
    photos=Photo.objects.all()
    context={'categories': categories,'photos':photos}
    return render(request,'photos/gallery.html',context) 

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    context={'photo':photo}
    return render(request,'photos/view_photo.html',context) 

def addPhoto(request):
    categories=Category.objects.all()
    if request.method=='POST':
        data =request.POST
        image=request.FILES.get('image')
        if data['category'] != 'none':
            category=Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category,created =Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category=None

        photo =Photo.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )
        
        
    context={'categories': categories}
    return render(request,'photos/add.html',context) 
