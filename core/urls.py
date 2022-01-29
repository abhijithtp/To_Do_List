from django.urls import path 
from . import views 
urlpatterns = [
    path('',views.Index,name='index'),
    path('deta/<str:ids>',views.Data,name='deta'),
    path('btn',views.Button,name='Button'),
    path('delete/<str:idd>',views.Delt,name='delete'),
    path('signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),

]
