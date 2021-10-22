# coding: utf-8
from django.shortcuts import render, redirect
from jobsearch.models import *
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import JobOfferForm


def home(request):
    """
    Method to render the homepage template
    """
    return render(request, 'pages/home.html')


def legal_notices(request):
    """
    Method to render the legal notices template
    """
    return render(request, 'pages/legal_notices.html')


def contact(request):
    """
    Method to render the contact template
    """
    return render(
        request,
        'pages/contact.html'
    )


@login_required(login_url='login')
def add_category(request):
    """
    Method to add a category on the user dashboard
    """
    user = request.user
    cat_name = request.GET.get('add_category')
    try:
        Categories.objects.create(
            user_id=user.id,
            name_category=cat_name
        )

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
        categories_view = Categories.objects.filter(
            user_id=user.id
        ).order_by('id')

        context = {
            'cat': categories_view
        }

    except ObjectDoesNotExist:
        return render(
            request,
            'pages/categories.html'
        )

    return render(
        request,
        'pages/categories.html',
        context
    )


@login_required(login_url='login')
def enter_category(request, id_cat):
    """
    Method to enter the category and see
    which job offer are already saved in
    """
    user = request.user
    cat_name = Categories.objects.get(
        user_id=user.id,
        id=id_cat
    )
    basic_job_info = JobOffer.objects.filter(
        user_id=user.id,
        category_id=id_cat
    )

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

    return render(
        request,
        'pages/enter_category.html',
        context
    )


@login_required(login_url='login')
def delete_category(request, cat_id):
    """
    Method to delete a category only if it is empty
    """
    user = request.user
    cat_content = JobOffer.objects.filter(
        category_id__id=cat_id
    )
    cat_to_delete = Categories.objects.get(
        user_id=user.id,
        id=cat_id
    )
    if not cat_content:
        cat_to_delete.delete()
        messages.success(request, 'category deleted')

        return redirect('home')

    else:
        messages.info(
            request,
            'This category is not empty and cannot be deleted'
        )

        return redirect('see_categories')


def job_offers_views(request, cate_id):
    """
    Function to render the jobs attached to a category
    No conditions have been made because
    the view is not called if there no job_offer to show
    """
    user = request.user
    jobs = JobOffer.objects.filter(
        user_id=user,
        category_id_id=cate_id
    ).order_by('date')

    all_status = Status.objects.all()
    category_concerned = cate_id

    status = {
        'all_status': all_status,
        'category_concerned': category_concerned
    }

    context = {
        'jobs': jobs,
        'status': status,
    }

    return render(
        request,
        'pages/job_description.html',
        context
    )


class JobOfferDetailView(DetailView):
    """
    Class with basicview to render
    the details of a specific job offer
    """
    model = JobOffer
    template_name = 'pages/job_detail.html'


class CreateJobOffer(CreateView):
    """
    Class with basicview to render
    a formular for creating a job offer
    """
    model = JobOffer
    form_class = JobOfferForm
    template_name = 'pages/add_job.html'


class UpdateJobOffer(UpdateView):
    """
    Class with basicview to render
    a formular to update
    the informations from a job offer
    """
    model = JobOffer
    form_class = JobOfferForm
    template_name = 'pages/update_job_offer.html'


class DeleteJobOffer(DeleteView):
    """
    Class with basic view
    to delete a specific job offer
    """
    model = JobOffer
    template_name = 'pages/delete_job_offer.html'
    success_url = reverse_lazy('home')


@login_required(login_url='login')
def select_status(request, status_id, catid):
    """
    Method to select a status and paginate all
    the job offer belonging to this status
    """
    user = request.user
    status_filtered = JobOffer.objects.filter(
        user_id=user,
        category_id=catid,
        status_id=status_id)\
        .order_by('date'
                  )

    if not status_filtered:
        messages.info(
            request,
            'No jobs saved under this status yet'
        )
        return render(request, 'pages/status_select.html')

    else:
        context = {
            'status_filtered': status_filtered,
            'category_concerned': catid
        }

        return render(
            request,
            'pages/status_select.html',
            context
        )


