from django.urls import path
from .views import Add_Room_Form_View,View_Rooms,test,Added_Room,Book_Rooms,User_Booked_Rooms,Available_rooms


urlpatterns=[

path('add_room_form/',Add_Room_Form_View,name='Add_Room_Form'),
path('room_lists/',View_Rooms,name='room_lists'),
path('booked_room/',test),
path('added-rooms/',Added_Room,name='Added_room'),
path('book/<int:id>/', Book_Rooms,name="Book"),
path('booked_rooms/',User_Booked_Rooms,name="Booked"),
path('available_rooms/',Available_rooms,name="available_rooms")

]