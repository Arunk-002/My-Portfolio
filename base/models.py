from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=100)
    message=models.TextField()
    def __str__(self):
        return 'message by '+ self.name