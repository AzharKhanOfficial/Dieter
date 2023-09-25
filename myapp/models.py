from django.db import models

# Create your models here.
class Diet(models.Model):
        name=models.TextField()
        desc= models.TextField()
        image= models.ImageField(upload_to='pics')
        url=models.TextField()

        