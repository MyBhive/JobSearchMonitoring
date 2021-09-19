# coding: utf-8
from django.urls import path
from django.contrib.auth.views import PasswordResetView, \
    PasswordResetDoneView, \
    PasswordResetConfirmView, \
    PasswordResetCompleteView
from . import views

"""Path to connect views to the frontend"""

urlpatterns = [
    path('login/', views.log_in, name="login"),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('log_out/', views.log_out, name='log_out'),

    path('password_reset/',
         PasswordResetView.as_view(
             template_name='userpages/reset_password.html'
         ),
         name='password_reset'),

    path('password_reset/done/',
         PasswordResetDoneView.as_view(
             template_name='userpages/password_reset_done.html'
         ),
         name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='userpages/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),

    path('password_reset/complete/',
         PasswordResetCompleteView.as_view(
             template_name='userpages/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    path('my_account/', views.my_account, name='my_account'),
]
