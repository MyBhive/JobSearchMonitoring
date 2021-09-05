# coding: utf-8
from django.shortcuts import render


def home(request):
    """Method to render the homepage template"""
    return render(request, 'pages/index.html')
