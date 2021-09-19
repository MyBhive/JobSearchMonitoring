# coding: utf-8
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('legal_notices', views.legal_notices, name='legal_notices'),
    path('contact', views.contact, name='contact'),
    path('see_categories', views.see_categories, name='see_categories'),
    path('add_categories', views.add_category, name='add_categories'),
    path('enter_category/<str:id_cat>/', views.enter_category, name='enter_category'),
    path('delete_category/<str:cat_id>', views.delete_category, name='delete_category'),
    path('add_job_offer', views.add_job_offer, name='add_job_offer'),
    path('job_description', views.see_job_offer, name='job_description'),
]
