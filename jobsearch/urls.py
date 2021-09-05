# coding: utf-8
from django.urls import path

from jobsearch.views import home

urlpatterns = [
    path('', home, name='pages/index'),
]