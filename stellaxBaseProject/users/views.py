from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, EditProfileForm, CustomPasswordChangeForm


def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"],
            )
            login(request, new_user)
            return redirect("home")
    else:
        form = RegisterForm()

    context = {"form": form}

    return render(request, "registration/register.html", context)


@login_required
def profile_view(request):

    context = {}
    return render(request, "users/profile.html", context)


@login_required
def user_settings(request):

    context = {}
    return render(request, "wip.html", context)


@login_required
def edit_profile(request):

    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:  # GET Post
        form = EditProfileForm(instance=request.user)

    context = {"form": form}
    return render(request, "users/edit_profile.html", context)


@login_required
def change_password(request):

    if request.method == "POST":
        form = CustomPasswordChangeForm(data=request.POST, user=request.user)
        
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("profile")
        else:
            return redirect("profile/change-password")

    else:
        form = CustomPasswordChangeForm(user=request.user)

    context = {"form": form}
    return render(request, "users/change_password.html", context)
