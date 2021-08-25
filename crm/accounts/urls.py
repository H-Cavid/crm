from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('products/',products,name='products'),
    path('customer/<str:pk>/',customer,name='customer'),
    path('create_order/<str:pk>',create_order,name='create_order'),
    path('update_order/<str:pk>',update_order,name='update_order'),
    path('delete_order/<str:pk>',delete_order,name='delete_order'),
    path('login/',loginPage,name='login'),
    path('register/',registerPage,name='register'),
    path('logout/',logoutUser,name='logout'),
    path('user/',userPage,name='user-page'),
    path('account/',accountSettings,name='account'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = 'accounts/password_reset.html'),name='reset_password'),#class based view olduguna gore as_view() yazilir||templaete_naem-in icinde oz htmlini gonderende onu acir
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = 'accounts/password_reset_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'),name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'accounts/password_reset_done.html'),name='password_reset_complete'),
]

# 1-Submit email form                        //PasswordResetView.as_view()
# 2-Email sent succes message                //PasswordResetDoneView.as_view() 
# 3-Link to password Rest form in email      //PasswordResetConfirmView.as_view()
# 4-Password succesfully changed message     //PasswordResetCompleteView.as_view()
#hamsi auth_views-un icindedi viewlar