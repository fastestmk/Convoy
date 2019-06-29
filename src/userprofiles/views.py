from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import SignUpForm, EditProfileForm, ProfileUpdateForm


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been logged in!'))
            return redirect('post:list')
        else:
            messages.success(request, ('Error logining in - please try again'))
            return redirect('Profile:sign_in')
    else:
        return render(request, 'login.html', {})


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You have registered'))
            return redirect('post:list')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'register.html', context)


def sign_out(request):
    logout(request)
    messages.success(request, ('You have been logged out'))
    return redirect('post:list')


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if form.is_valid() and p_form.is_valid():
            form.save()
            p_form.save()
            messages.success(request, ('You have edited you profile.'))
            return redirect('Profile:edit_profile')
    else:
        form = EditProfileForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'form': form,
        'p_form': p_form
    }
    return render(request, 'edit_profile.html', context)


def user_profile(request):
    return render(request, 'profile.html', {})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ('You have edited you password.'))
            return redirect('Profile:home')
    else:
        form = PasswordChangeForm(user=request.user)

    context = {'form': form}
    return render(request, 'change_password.html', context)
