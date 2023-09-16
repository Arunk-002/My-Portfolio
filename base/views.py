from django.shortcuts import render
from base.models import Contact
# Create your views here.

def Home(request):
    return render(request,'base/index.html')
def Contact_view(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        print(name,email,message)
        contact = Contact(name=name, email=email, message=message)
        contact.save()
    return render(request,'base/contact.html')