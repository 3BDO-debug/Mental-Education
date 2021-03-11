from django.db import models
from Accounts.models import User
from Courses.models import Course
# Create your models here.
class Wishlist(models.Model):
    related_account = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Related Account") 
    wished_courses = models.ManyToManyField(Course, blank=True, verbose_name = "Wished Courses")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    class Meta:
        verbose_name = "Wishlist"
        verbose_name_plural = "Wishlists"

    def __str__(self):
        return f"Wishlist for {self.related_account.user_full_name}"

class StaffMember(models.Model):
    related_teacher_account = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Related Teacher Account")
    staff_member_pic = models.ImageField(upload_to='Staff_Members_Photos', verbose_name="Staff Member Picture")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    class Meta:
        verbose_name = "Staff Member"
        verbose_name_plural = "Staff Members"

    def __str__(self):
        return self.staff_member_pic.name


class BestStudent(models.Model):
    student_pic = models.ImageField(upload_to="Best_Students_Photos", verbose_name="Student Pic")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")


    class Meta:
        verbose_name = "Best Student"
        verbose_name_plural = "Best Students"

    def __str__(self):
        return self.student_pic.name