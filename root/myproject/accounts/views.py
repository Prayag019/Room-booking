from django.shortcuts import render,redirect
from django.views.generic import CreateView,TemplateView,FormView
from .models import CustomUser,Rooms
from .forms import SignupForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout as auth_logout


# Create your views here.


def test(request):
    pass



class SignupView(CreateView):
    model=CustomUser
    template_name='accounts/signup.html'
    form_class=SignupForm
    success_url=reverse_lazy('login_page')


    def form_invalid(self, form):
        print("errors:",form.errors)
        messages.error(self.request,"form is invalid")
        return super().form_invalid(form)



def SignupView(request):
    if request.method == "POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
        else:
            messages.error(request,"form is invalid")  
    else:
        form=SignupForm()
    return render(request,"accounts/signup.html",{'form':form})   





class Dashboard(LoginRequiredMixin,TemplateView):
    template_name='rooms/dashboard.html'




def Login(request):
    if request.method=='POST':

        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
           user=form.get_user()
           auth_login(request,user)
           messages.success(request,"logged in succesfully")
           return redirect('Dashboard')
        else:
           print(form.errors)
           messages.error(request,"Invalid username or password") 
    else:
        form=AuthenticationForm()
    return render(request,'accounts/login.html',{'form': form})
          


def Logout(request):
    auth_logout(request)
    redirect('login')




