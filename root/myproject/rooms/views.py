from django.shortcuts import render,redirect
from accounts.models import Rooms
from accounts.forms import Add_Room_Form
from django.db.models import Q
from django.contrib.auth.decorators import login_required



def test(request):
    pass


def View_Rooms(request):

    city=request.GET.get('city')
    room=request.GET.get('room')
    rent=request.GET.get('rent')

    filters=Q(is_approved=True) & Q(is_booked=False)
    if city:
        filters &=Q(city__icontains=city)
    if rent:
        filters &=Q(rent=rent)
    if room:
        filters &=Q(room_type__icontains=room)   

    rooms=Rooms.objects.filter(filters)   
          
    
    return render(request,'rooms/room_lists.html',{'rooms':rooms})
    
def Add_Room_Form_View(request):
    if request.method=='POST':
        form=Add_Room_Form(request.POST)
        if form.is_valid():
            room=form.save(commit=False)
            room.owner=request.user
            room.save()

            return redirect('Added_room')


    
    else:
        form=Add_Room_Form()

        return render(request,'rooms/Add_Room_Form.html',{'form':form})  











   



def Delete_Rooms(request):
   pass
def Book_Rooms(request,id):
 
   room=Rooms.objects.get(id=id)
   room.is_booked=True
   room.booked_by=request.user
   room.save()
   return redirect('Booked')

   






           

def Added_Room(request):


   rooms=Rooms.objects.filter(owner=request.user)
   pending_rooms=rooms.filter(is_approved=False)
   approved_rooms=rooms.filter(is_approved=True)
   context={}
   if pending_rooms.exists():
        context['pending']=pending_rooms
   if approved_rooms.exists():
        context['approved']=approved_rooms
   return render(request,'rooms/added_rooms.html',context)        



def User_Booked_Rooms(request):

    user=request.user 
    room=Rooms.objects.filter(booked_by=user)
    return render(request,'rooms/my_rooms.html',{'rooms':room})



