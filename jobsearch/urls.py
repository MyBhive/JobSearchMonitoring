from django.urls import path

from jobsearch.views import index

urlpatterns = [
    path('', index, name='index'),
]