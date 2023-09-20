from django.urls import path
from .import views

urlpatterns = [
    path('', views.Home),
    path('contact',views.Contact_view,name="contact"),
]
