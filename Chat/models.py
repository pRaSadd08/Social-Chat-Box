from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Social(models.Model):
    class Meta(object):
        db_table='post'

    name = models.CharField('Name', max_length=15, null=False, blank=False, db_index=True, default='Anonymous')

    body = models.CharField('Body', max_length=150, null=False, blank=False, db_index=True)

    DateTime = models.DateTimeField('DateTime',auto_now_add=True, blank=True)

    image = CloudinaryField('image',blank=True)
    
    likes= models.PositiveIntegerField('Likes', default=0,null=True, blank=True)
   
  
    def __str__(self):
     return self.name