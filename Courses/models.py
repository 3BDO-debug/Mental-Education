from django.db import models
from Accounts.models import User
from Educational_Stages.models import Subject
from django.utils.text import slugify
from admin_resumable.fields import ModelAdminResumableFileField

# Create your models here.
"""class CourseCategory(models.Model):
    category_name = models.CharField(verbose_name="Category Name", max_length=300)
    category_name_as_slug = models.SlugField(
        max_length=350, verbose_name="Category Name as Slug", default="slug-here"
    )
    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)

    class Meta:
        verbose_name = "Course Category"
        verbose_name_plural = "Course Categories"

    def save(self, *args, **kwargs):
        self.category_name_as_slug = slugify(self.category_name)
        super(CourseCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name"""


class Course(models.Model):
    course_name = models.CharField(verbose_name="Course Name", max_length=300)
    course_thumbnail = models.ImageField(
        verbose_name="Course's Thumbnail",
        upload_to="Courses_Thumbnails",
        default="course-thumbnail.png",
    )
    course_trailer_video = models.FileField(
        verbose_name="Course's Trailer Video",
        upload_to="Courses_Trailers",
        default="course-trailer.mp4",
    )
    course_description = models.TextField(
        verbose_name="Course Description", default="Course Description Goes here."
    )
    tutored_by = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Tutored By"
    )
    course_name_as_slug = models.SlugField(
        max_length=350, verbose_name="Course Name as Slug", default="slug-here"
    )
    related_subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, verbose_name="Related Subject"
    )

    attached_PDF = models.FileField(null=True, verbose_name="Attach PDF", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def save(self, *args, **kwargs):
        self.course_name_as_slug = slugify(self.course_name)
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.course_name


class CourseLesson(models.Model):
    related_course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Related Course"
    )
    lesson_name = models.CharField(verbose_name="Lesson Name", max_length=300)
    lesson_video_file = ModelAdminResumableFileField()
    lesson_video_link = models.CharField(
        verbose_name="Lesson Video Link", max_length=700, null=True, blank=True
    )
    added_at = models.DateTimeField(verbose_name="Added at", auto_now_add=True)

    class Meta:
        verbose_name = "Course Lesson"
        verbose_name_plural = "Course Lessons"

    def __str__(self):
        return self.lesson_name


