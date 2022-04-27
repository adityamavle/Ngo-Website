from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about/', views.about,name='about'),
    path('login/', views.login,name='login'),
    path('signup/', views.signup,name='signup'),
    path('agriculture/', views.agriculture, name='agriculture'),
    path('childcare/', views.childcare, name='childcare'),
    path('education/', views.education, name='education'),
    path('healthcare/',views.healthcare,name='healthcare'),
    path('help/', views.help,name='help'),
    path('wildlife_1/',views.wildlife_1,name='wildlife_1'),
    path('wildlifenecology',views.wildlifenecology,name='wildlifenecology'),
    path('womendev/',views.womendev,name='womendev'),

]