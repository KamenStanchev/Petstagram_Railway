from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import forms, authenticate, login, logout, update_session_auth_hash
from django.views import generic

from main_app.forms import EditProfileForm
from main_app.models import Profile, Pet, PetPhoto


def create_account(request):
    form = forms.UserCreationForm()

    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created with username: ' + user)
            return redirect('login_page')

    context = {'form': form, }
    return render(request, 'create_account.html', context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'User was successful log-in')
            return redirect('dashboard')
        else:
            messages.error(request, 'User or passwowrd is invalid')

    form = forms.AuthenticationForm
    context = {'form': form, }
    return render(request, 'login_page.html', context)


@login_required(login_url=login_page)
def logout_page(request):
    logout(request)
    messages.success(request, 'User was successful LogOut')
    return redirect('home_page')

@login_required(login_url='login_page')
def account_details(request):
    current_account = request.user
    profile = Profile.objects.filter(account_id=current_account.id)
    photos = PetPhoto.objects.filter(account_id=current_account.id)
    total_images = len(photos)
    total_likes = sum(p.likes for p in photos)
    pets = Pet.objects.filter(account=current_account)
    if profile:
        context = {
            'profile': profile[0],
            'pets': pets,
            'total_images': total_images,
            'total_likes': total_likes,
        }
        return render(request, 'account_details.html', context)
    return redirect('create_profile')


class AccountsListView(generic.ListView):
    template_name = 'accounts_list.html'
    model = User
    context_object_name = 'users'



@login_required(login_url='login_page')
def edit_account(request):
    current_account = request.user
    current_profile = Profile.objects.get(account=current_account)
    if current_profile is None:
        return redirect('create_profile')
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=current_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile was updated')
            return redirect('account_detail')
        else:
            messages.error(request, 'Form is not valid')

    form = EditProfileForm(instance=current_profile)
    context = {
        'form': form,
        'account': current_account,
        'profile': current_profile,
    }
    return render(request, 'edit_account.html', context)


@login_required
def edit_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('account_detail')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'edit_password.html', {
        'form': form
    })
