from . import views
from django.urls import path

urlpatterns = [
    path('Add-New-Review/To/<slug:course_name_as_slug>', views.course_review_handler)
]