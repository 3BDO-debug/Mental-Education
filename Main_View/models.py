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