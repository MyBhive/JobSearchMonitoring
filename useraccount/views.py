from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

#from jobsearch.models import
from .forms import SignInForm


def sign_in(request):
    """Method to allow the user to create an account"""
    form = SignInForm()
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('email')
            messages.success(request,
                             'Compte ustilisateur créé pour '
                             + user
                             )
            return redirect('login')

    context = {'form': form}

    return render(request, 'userpages/sign_in.html', context)


def log_in(request):
    """Method to allow the user to log in to his account"""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request,
                            username=email,
                            password=password
                            )

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.info(request,
                          'Identifiant ou mot de passe incorrect'
                          )

    return render(request, 'userpages/login.html')


def log_out(request):
    """django method to log out from your user account"""
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def my_account(request):
    """Method To render the user account information's template"""
    return render(request, 'userpages/my_account.html')


def change_email(request):
    pass


def change_password(request):
    pass

