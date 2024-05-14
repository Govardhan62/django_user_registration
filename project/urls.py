from django.urls import path
from project.views import home,enter,inside,table,logout

urlpatterns = [
    path('',home,name='home'),
    path('enter',enter,name='enter'),
    path('inside',inside,name='inside'),
    path('table',table,name='table'),
     path('logout',logout,name='logout'),


]