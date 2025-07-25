from django.urls import  path
from .views import test,SignupView,Dashboard,Login,Logout


urlpatterns=[

path('test/',test),
path('signup/',SignupView,name='signup'),
path('dash-board/',Dashboard.as_view(),name='Dashboard'),
path('login_form/',Login,name='login'),
path('logout/',Logout,name="logout")

]