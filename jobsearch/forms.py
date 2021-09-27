from django.views.generic import CreateView
from jobsearch.models import *


class CreateJobOffer(CreateView):
    model = JobOffer
    template_name = 'pages/add_job.html'
    fields = (
        'title',
        'company_name',
        'url',
        'date',
        'salary',
        'comments',
        'status_id',
        'style_id',
        'type_id',
    )
