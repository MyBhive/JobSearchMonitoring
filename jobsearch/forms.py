from django.views.generic import CreateView
from jobsearch.models import *
from django import forms


class CreateJobOffer(CreateView):
    model = JobOffer

    template_name = 'pages/add_job.html'
    fields = '__all__'


