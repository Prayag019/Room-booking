from django.db import models
from accounts.models import CustomUser,Rooms

# Create your models here.
class Booked_Rooms(models.Model):
	room_owner=models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='Room_owner')
	booked_by=models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='Booked_user')
	booked_room=models.OneToOneField(Rooms,on_delete=models.CASCADE)
	booked_at=models.DateTimeField(auto_now_add=True)
class Added_Rooms(models.Model):
	owner=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
	added_time=models.DateTimeField(auto_now_add=True)




