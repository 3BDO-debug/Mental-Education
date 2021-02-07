from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . import models
from Main_View.models import Wishlist
from Mental_Learning.auth_token import auth_token_generator

# Create your views here.
def register_handler(request):
    user_full_name = request.POST.get("user_full_name")
    user_email = request.POST.get("user_email")
    user_password = request.POST.get("user_password")
    user_confirm_password = request.POST.get("user_confirm_password")

    if user_password == user_confirm_password:
        try:
            user = models.User.objects.create_user(
                user_full_name=user_full_name,
                user_email=user_email,
                password=user_password,
            )
            create_wishlist_instance = Wishlist.objects.create(
                related_account=user
            ).save()
            messages.success(
                request,
                f"Hey {user_full_name} your account had been successfully created and we had sent you confirmation mail",
            )
            email_confirmation_token = auth_token_generator()
            request.session[
                "email_confirmation_token"
            ] = email_confirmation_token  # storing the token inside a session variable
            subject = "Mental Learner"
            message = "Confirm Your Email on Mental Learner"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [
                user.user_email,
            ]
            html_message = render_to_string(
                "ConfirmEmail.html",
                {
                    "user_id": user.id,
                    "user_full_name": user.user_full_name,
                    "email_confirmation_token": email_confirmation_token,
                },
            )
            plain_message = strip_tags(html_message)
            send_mail(
                subject=subject,
                message=plain_message,
                from_email=from_email,
                recipient_list=recipient_list,
                html_message=html_message,
            )
            return redirect("/View/Auth/Register")
        except IntegrityError:
            messages.error(
                request,
                f"Hey {user_full_name} account with this email already exist, Login Instead.",
            )
            return redirect("/View/Auth/Register")
        else:
            return render(request, "ErrorOccured.html")
    else:
        messages.error(request, f"{user_full_name} your password doesn't match.")
        return redirect("/View/Auth/Register")


def login_handler(request):
    user_email = request.POST.get("user_email")
    user_password = request.POST.get("user_password")
    if authenticate(user_email=user_email, password=user_password):
        login(request, authenticate(user_email=user_email, password=user_password))
        return redirect(
            (
                "/View/Student-Profile-Settings"
                if not request.user.is_teacher
                else "/View/Teacher-Profile"
            )
        )
    else:
        messages.error(request, f"wrong email or password")
        return redirect("/View/Auth/Login")


def logout_handler(request):
    logout(request)
    return render(request, "Logout.html")


def email_confirmation_handler(request, user_id, email_confirmation_token):
    if email_confirmation_token == request.session.get("email_confirmation_token"):
        user_to_be_activated = models.User.objects.get(id=user_id)
        user_to_be_activated.is_active = True
        user_to_be_activated.save()
        return redirect("/View/Activate-Me/Email-Confirmed")
    else:
        return redirect("/View/Activate-Me/Email-Not-Confirmed")


def account_data_handler(request):
    account_to_be_edited = models.User.objects.get(id=int(request.POST.get("user_id")))
    account_to_be_edited.user_full_name = request.POST.get("user_full_name")
    account_to_be_edited.user_email = request.POST.get("user_email")
    account_to_be_edited.selected_subjects.set(
        [
            int(selected_subject)
            for selected_subject in request.POST.getlist("selected_subjects")
        ]
    )
    account_to_be_edited.save()
    return redirect("/View/Student-Profile")