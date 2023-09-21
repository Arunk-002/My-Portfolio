from django.urls import path
from photos import views

app_name = 'photos'

urlpatterns = [
    path('gallery',views.Gallery,name="gallery"),
    path('photo/<int:pk>/', views.viewPhoto, name="photo"),
    path('viewpic/', views.view, name="viewpic"),
    path('add/',views.addPhoto,name="add"),
]
