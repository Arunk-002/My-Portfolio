from django.urls import path
from photos import views

app_name = 'photos'

urlpatterns = [
    path('gallery',views.Gallery,name="gallery"),
    path('photo/<int:pk>/', views.viewPhoto, name="photo"),
    path('add/',views.addPhoto,name="add"),
]
