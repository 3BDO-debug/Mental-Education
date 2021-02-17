from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models
from Courses import models as Courses_Models
from Courses_Reviews import models as Course_Reviews_Models
from Educational_Stages import models as Edu_Stages_Models

# Create your views here.
def get_main_view_data(request):
    edu_stages = Edu_Stages_Models.EducationlStage.objects.all()
    recently_added_courses = Courses_Models.Course.objects.all().order_by("-created_at")

    if request.user.is_authenticated:
        user_wishlist = get_object_or_404(models.Wishlist, related_account=request.user)
        main_data = {
            "user_wishlist": user_wishlist,
            "edu_stages": edu_stages,
            "recently_added_courses": recently_added_courses,
        }
        return main_data
    else:
        main_data = {
            "edu_stages": edu_stages,
            "recently_added_courses": recently_added_courses,
        }
        return main_data


def course_reviews_data(course_name_as_slug):
    course_reviews = Course_Reviews_Models.CourseReview.objects.filter(
        related_course=Courses_Models.Course.objects.get(
            course_name_as_slug=course_name_as_slug
        )
    )

    return course_reviews


def search_handler(request):
    main_view_data = get_main_view_data(request)

    search = request.GET.get("search")
    search_results = Courses_Models.Course.objects.filter(course_name__contains=search)
    if request.user.is_authenticated:
        return render(
            request,
            "SearchResult.html",
            {
                "search_results": search_results,
                "categories": main_view_data["categories"],
                "user_wishlist": main_view_data["user_wishlist"],
            },
        )
    else:
        return render(
            request,
            "SearchResult.html",
            {
                "search_results": search_results,
                "categories": main_view_data["categories"],
            },
        )


def home_page(request):
    staff_members = models.StaffMember.objects.all().order_by("-created_at")
    best_students = models.BestStudent.objects.all().order_by("-created_at")
    main_view_data = get_main_view_data(request)

    if request.user.is_authenticated:
        return render(
            request,
            "HomePage.html",
            {
                "edu_stages": main_view_data["edu_stages"],
                "staff_members": staff_members,
                "best_students": best_students,
                "user_wishlist": main_view_data["user_wishlist"],
                "recently_added_courses": main_view_data["recently_added_courses"],
            },
        )
    else:
        return render(
            request,
            "HomePage.html",
            {
                "edu_stages": main_view_data["edu_stages"],
                "staff_members": staff_members,
                "best_students": best_students,
                "recently_added_courses": main_view_data["recently_added_courses"],
            },
        )


def edu_stage_levels_page(request, edu_stage_id):
    main_view_data = get_main_view_data(request)

    edu_stage_levels = Edu_Stages_Models.EducationStageLevel.objects.filter(
        related_edu_stage=edu_stage_id
    )
    if request.user.is_authenticated:
        return render(
            request,
            "EduStageLevels.html",
            {
                "edu_stages": main_view_data["edu_stages"],
                "user_wishlist": main_view_data["user_wishlist"],
                "edu_stage_levels": edu_stage_levels,
            },
        )
    else:
        return render(
            request,
            "EduStageLevels.html",
            {
                "edu_stages": main_view_data["edu_stages"],
                "edu_stage_levels": edu_stage_levels,
            },
        )


def edu_stage_level_subjects_page(request, edu_stage_level_id):
    main_view_data = get_main_view_data(request)

    edu_stage_level_subjects = Edu_Stages_Models.Subject.objects.filter(
        related_edu_stage_level=edu_stage_level_id
    )
    if request.user.is_authenticated:
        return render(
            request,
            "EduStageLevelSubjects.html",
            {
                "edu_stages": main_view_data["edu_stages"],
                "user_wishlist": main_view_data["user_wishlist"],
                "edu_stage_level_subjects": edu_stage_level_subjects,
            },
        )
    else:
        return render(
            request,
            "EduStageLevelSubjects.html",
            {
                "edu_stages": main_view_data["edu_stages"],
                "edu_stage_level_subjects": edu_stage_level_subjects,
            },
        )


def courses_page(request, related_edu_stage_level_subject_id):
    main_view_data = get_main_view_data(request)

    page = request.GET.get("page", 1)

    category_courses = Courses_Models.Course.objects.filter(
        related_subject=related_edu_stage_level_subject_id
    ).order_by("-created_at")
    paginator = Paginator(category_courses, 4)
    paginator_status = paginator.page(page)
    category_courses = paginator_status.object_list

    if request.user.is_authenticated:

        return render(
            request,
            "Courses.html",
            {
                "courses": category_courses,
                "num_of_pages": paginator.page_range,
                "paginator_status": paginator_status,
                "edu_stages": main_view_data["edu_stages"],
                "user_wishlist": main_view_data["user_wishlist"],
            },
        )
    else:
        return render(
            request,
            "Courses.html",
            {
                "courses": category_courses,
                "num_of_pages": paginator.page_range,
                "paginator_status": paginator_status,
                "edu_stages": main_view_data["edu_stages"],
            },
        )


def course_intro_page(request, course_name_as_slug):
    main_view_data = get_main_view_data(request)

    course = Courses_Models.Course.objects.get(course_name_as_slug=course_name_as_slug)
    if request.user.is_authenticated:
        return render(
            request,
            "CourseIntro.html",
            {
                "course": course,
                "course_reviews": course_reviews_data(course_name_as_slug),
                "edu_stages": main_view_data["edu_stages"],
                "user_wishlist": main_view_data["user_wishlist"],
            },
        )
    else:
        return render(
            request,
            "CourseIntro.html",
            {
                "course": course,
                "course_reviews": course_reviews_data(course_name_as_slug),
                "edu_stages": main_view_data["edu_stages"],
            },
        )


def course_details_page(request, course_name_as_slug):
    main_view_data = get_main_view_data(request)

    course = Courses_Models.Course.objects.get(course_name_as_slug=course_name_as_slug)
    related_courses = Courses_Models.Course.objects.filter(
        related_subject=course.related_subject
    )[0:2]
    return render(
        request,
        "CourseDetails.html",
        {
            "course": course,
            "course_reviews": course_reviews_data(course_name_as_slug),
            "related_courses": related_courses,
            "edu_stages": main_view_data["edu_stages"],
            "user_wishlist": main_view_data["user_wishlist"],
        },
    )


def course_content_page(request, course_name_as_slug):
    course = Courses_Models.Course.objects.get(course_name_as_slug=course_name_as_slug)

    return render(
        request,
        "CourseContent.html",
        {
            "course": course,
        },
    )


def quizes_page(request):
    return render(request, "Quizes.html")


def quiz_page(request):
    return render(request, "Quiz.html")


def teacher_profile_page(request):
    return render(request, "TeacherProfile.html")


def student_profile_page(request):
    main_view_data = get_main_view_data(request)

    return render(
        request,
        "StudentProfile.html",
        {
            "edu_stages": main_view_data["edu_stages"],
            "user_wishlist": main_view_data["user_wishlist"],
        },
    )


def student_profile_settings_page(request):
    main_view_data = get_main_view_data(request)

    return render(
        request,
        "StudentProfileSettings.html",
        {
            "edu_stages": main_view_data["edu_stages"],
            "user_wishlist": main_view_data["user_wishlist"],
        },
    )


def authentication_pages(request, condition):
    if condition == "Register":
        return render(request, "Register.html")
    elif condition == "Login":
        return render(request, "Login.html")


def email_confirmation_status_page(request, condition):

    account_activation_status = True if condition == "Email-Confirmed" else False
    return render(
        request,
        "EmailConfirmationStatus.html",
        {"account_activation_status": account_activation_status},
    )


def wishlist_handler(request, course_id):
    user_wishlist = get_main_view_data(request)
    user_wishlist = user_wishlist["user_wishlist"]
    user_wishlist.wished_courses.add(course_id)
    user_wishlist.save()
    return HttpResponse("Course Added to wishlist")
