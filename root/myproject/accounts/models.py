from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    contact_number=models.CharField(max_length=10)
    full_name=models.CharField(max_length=100)


class Rooms(models.Model):
    owner=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='owned_rooms')
    room_type=models.CharField(max_length=4)
    city=models.CharField(max_length=15)
    full_address=models.CharField(max_length=50)
    rent=models.IntegerField()
    is_approved=models.BooleanField(default=False)
    facilities=models.TextField()
    is_booked=models.BooleanField(default=False,blank=False,null=True)
    booked_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='booked_rooms',default=None,blank=True,null=True)
   


class Image(models.Model):
    image=models.ImageField(upload_to='room_images/',default=None,null=True)
    room=models.ForeignKey(Rooms,on_delete=models.CASCADE,related_name='image')




