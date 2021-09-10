# coding: utf-8
from django.shortcuts import render


def home(request):
    """Method to render the homepage template"""
    return render(request, 'pages/home.html')


def legal_notices(request):
    """Method to render the legal notices template"""
    return render(request, 'pages/mentions_legales.html')


def contact(request):
    """Method to render the contact template"""
    return render(request, 'pages/contact.html')


def add_category(request):
    """
    Method to add a category on the user dashboard
    """
    pass


def see_categories(request):
    """
    Method to see which are the different
    categories already saved by the user
    """
    pass


def enter_category(request):
    """
    Method to enter the category and see
    which job offer are already saved in
    """
    pass


def add_job_offer(request):
    """
    Method to add a job offer and
    his description to a category
    """
    pass


def modify_job_offer(request):
    """
    Method to modify elements from a job offer
    """
    pass


def select_status(request):
    """
    Method to select a status and paginate all
    the job offer belonging to this status
    """
    pass


def see_job_offer(request):
    """
    Method to see the description and
    information inside a job offer card
    """
    pass


def delete_job_offer(request):
    """
    Method to delete a job offer from the database
    """
    pass


def modify_status_on_job_offer(request):
    """
    Method to update the status from a job offer
    """
    pass


def add_job_interview_on_job_offer(request):
    """
    Method to add date and time
    for a job interview to a job offer
    """
    pass


def search_job_offer_saved(request):
    """
    Method to find a job offer saved inside
    the database through the research bar
    """
    pass

