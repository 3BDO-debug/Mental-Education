from django.urls import path
from . import views

urlpatterns = [
    path("<int:edu_stage_id>/Levels", views.edu_stage_levels_page),
    path("<int:edu_stage_level_id>/Subjects", views.edu_stage_level_subjects_page),
    path("<int:related_edu_stage_level_subject_id>/Courses", views.courses_page),
    path("<slug:course_name_as_slug>/Course-Intro", views.course_intro_page),
    path("<slug:course_name_as_slug>/Course-Details", views.course_details_page),
    path("<slug:course_name_as_slug>/Course-Content", views.course_content_page),
    path("Quizes", views.quizes_page),
    path("Quiz", views.quiz_page),
    path("Teacher-Profile/<int:teacher_id>", views.teacher_profile_page),
    path("Student-Profile", views.student_profile_page),
    path("Student-Profile-Settings", views.student_profile_settings_page),
    path("Auth/<str:condition>", views.authentication_pages),
    path("Activate-Me/<str:condition>", views.email_confirmation_status_page),
    path("Wishlist/Course/<int:course_id>/Wished", views.wishlist_handler),
    path("Find-Course", views.search_handler),
]
