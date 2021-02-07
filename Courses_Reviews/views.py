from django.http import HttpResponse
from Courses.models import Course
from . import models

# Create your views here.
def course_review_handler(request, course_name_as_slug):
    models.CourseReview.objects.create(
        related_account=request.user,
        related_course=Course.objects.get(course_name_as_slug=course_name_as_slug),
        review_body=request.POST.get("review_body"),
    ).save()
    return HttpResponse("Review had been added")