from django.db import models
from Accounts.models import User
from Courses.models import Course
# Create your models here.
class CourseReview(models.Model):
    related_account = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Related Account")
    related_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Related Course")
    review_body = models.TextField(verbose_name="Review Body")

    class Meta:
        verbose_name = "Course Review"
        verbose_name_plural = "Course Reviews"

    def __str__(self):
        return f"New review by {self.related_account.user_full_name}"