from django.db import models

# Create your models here.
class receipe(models.Model):
    receipe_name=models.CharField(max_length=100,unique=True)
    receipe_description=models.TextField()
    receipe_image=models.ImageField(upload_to='receipe')
    
    