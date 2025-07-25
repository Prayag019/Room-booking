from django.urls import path
from .views import Add_Room_Form_View,View_Rooms,test,Added_Room,Book_Rooms,User_Booked_Rooms


urlpatterns=[

path('add-room-form/',Add_Room_Form_View,name='Add_Room_Form'),
path('room-lists/',View_Rooms,name='room-lists'),
path('booked_room/',test),
path('added-rooms/',Added_Room,name='Added_room'),
path('book/<int:id>/', Book_Rooms,name="Book"),
path('booked_rooms/',User_Booked_Rooms,name="Booked")

]