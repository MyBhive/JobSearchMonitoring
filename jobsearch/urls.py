# coding: utf-8
from django.urls import path
from .views import JobOfferView, JobOfferDetailView
from .forms import CreateJobOffer
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('legal_notices', views.legal_notices, name='legal_notices'),
    path('contact', views.contact, name='contact'),
    path('see_categories', views.see_categories, name='see_categories'),
    path('add_categories', views.add_category, name='add_categories'),
    path('enter_category/<str:id_cat>/', views.enter_category, name='enter_category'),
    path('delete_category/<str:cat_id>', views.delete_category, name='delete_category'),
    path('job_description/<int:id_cat>', JobOfferView.as_view(), name='job_description'),
    path('job_detail/<int:pk>', JobOfferDetailView.as_view(), name='job_detail'),
    path('add_job/<int:id_cat>', CreateJobOffer.as_view(), name='add_job'),
]
