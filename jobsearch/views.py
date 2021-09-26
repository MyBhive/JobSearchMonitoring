# coding: utf-8
from django.shortcuts import render, redirect
from jobsearch.models import *
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, ProgrammingError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.views.generic.detail import DetailView


class JobOfferView(ListView):
    model = JobOffer
    template_name = 'pages/job_description.html'


class JobOfferDetailView(DetailView):
    model = JobOffer
    template_name = 'pages/job_detail.html'


def home(request):
    """Method to render the homepage template"""
    return render(request, 'pages/home.html')


def legal_notices(request):
    """Method to render the legal notices template"""
    return render(request, 'pages/legal_notices.html')


def contact(request):
    """Method to render the contact template"""
    return render(request, 'pages/contact.html')


@login_required(login_url='login')
def add_category(request):
    """
    Method to add a category on the user dashboard
    """
    user = request.user
    cat_name = request.GET.get('add_category')
    try:
        Categories.objects.create(user_id=user.id, name_category=cat_name)

    except IntegrityError:

        messages.success(
            request,
            'You already created a category under this name. '
            'Please check my categories'
        )

        return redirect('home')

    return redirect('see_categories')


@login_required(login_url='login')
def see_categories(request):
    """
    Method to see which are the different
    categories already saved by the user
    """
    user = request.user
    try:
        categories_view = Categories.objects.filter(user_id=user.id).order_by('id')
        paginate = Paginator(categories_view, 99)
        page = request.GET.get('page')
        pag_num = paginate.get_page(page)

        context = {
            'page_num': pag_num,
            'paginate': True,
            'cat': categories_view
        }

    except ObjectDoesNotExist:
        return render(request, 'pages/categories.html')

    return render(request, 'pages/categories.html', context)


@login_required(login_url='login')
def enter_category(request, id_cat):
    """
    Method to enter the category and see
    which job offer are already saved in
    """
    user = request.user
    cat_name = Categories.objects.get(user_id=user.id, id=id_cat)
    basic_job_info = JobOffer.objects.filter(user_id=user.id, category_id=id_cat)

    if basic_job_info:
        context = {
            'title': cat_name,
            'id_cat': id_cat,
            'basic': basic_job_info
        }

    else:
        basic_job_info = []
        context = {
            'title': cat_name,
            'id_cat': id_cat,
            'basic': basic_job_info
        }

    return render(request, 'pages/enter_category.html', context)


@login_required(login_url='login')
def delete_category(request, cat_id):
    """
    Method to delete a category only if it is empty
    """
    user = request.user
    cat_to_delete = Categories.objects.get(user_id=user.id, id=cat_id)
    try:
        cat_to_delete.delete()
        messages.success(request, 'category deleted')

        return redirect('home')

    except ProgrammingError:
        messages.info(request, 'This category is not empty and cannot be deleted')

        return redirect('see_categories')


@login_required(login_url='login')
def add_job_offer(request):
    """
    Method to add a job offer and
    his description to a category
    """
    # create a forms.py and a formular first?
    return render(request, 'pages/add_job_offer.html')


@login_required(login_url='login')
def modify_job_offer(request):
    """
    Method to modify elements from a job offer
    """
    # queryset to modify. Conditions if request.GET.get('company_name') if ('name')
    pass


@login_required(login_url='login')
def select_status(request, status_id):
    """
    Method to select a status and paginate all
    the job offer belonging to this status
    """
    # status = inner join StatusConnect and Status to get the status id .order_by('id')
    pass


@login_required(login_url='login')
def see_job_offer(request, job_description):
    """
    Method to see the description and
    information inside a job offer card
    """
    user = request.user
    job = JobOffer.objects.get(user_id=user, id=job_description)

    context = {
        'title': job.title,
        'company_name': job.company_name,
        'url': job.url,
        'date': job.date,
        'salary': job.salary,
        'comments': job.comments
    }

    return render(request, 'pages/job_description.html', context)
    pass


@login_required(login_url='login')
def delete_job_offer(request, job_id):
    """
    Method to delete a job offer from the database
    """
    # add message are you sure you want to delete it yes/no
    user = request.user
    job_to_delete = JobOffer.objects.get(user_id=user, id=job_id)
    try:
        job_to_delete.delete()
        messages.success(request, 'job deleted')

        return redirect('enter_category')

    except ObjectDoesNotExist:
        messages.success(request, 'This job offer does not exist')

        return redirect('enter_category')
    pass

