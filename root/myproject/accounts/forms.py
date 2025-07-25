from django import forms
from .models import CustomUser,Rooms


class SignupForm(forms.ModelForm):
	class Meta:
		model=CustomUser
		fields=['username','password','email','first_name','last_name','contact_number']
		

class Add_Room_Form(forms.ModelForm):
	class Meta:
		model=Rooms
		exclude=['is_approved','owner','is_booked','booked_by']

		