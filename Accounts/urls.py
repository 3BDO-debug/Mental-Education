from django.urls import path
from . import views

urlpatterns = [
    path("Register", views.register_handler),
    path("Login", views.login_handler),
    path(
        "Activate-Me/<int:user_id>/<str:email_confirmation_token>",
        views.email_confirmation_handler,
    ),
    path("Logout", views.logout_handler),
    path("Edit-Profile", views.account_data_handler),
]