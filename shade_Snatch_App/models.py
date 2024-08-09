import os
from django.db import models

# Create your models here.
def custom_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    custom_filename = 'image_{}.{}'.format(instance.number, ext)
    return os.path.join('uploads', custom_filename)

class Image(models.Model):
    number= models.AutoField(primary_key=True)
    image= models.ImageField(upload_to='images/')
    # ref_number= self.number

    def __str__(self):
        return f"Image {self.number}"