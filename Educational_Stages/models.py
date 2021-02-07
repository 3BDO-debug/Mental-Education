from django.db import models
from django.utils.text import slugify

# Create your models here.


class EducationlStage(models.Model):
    edu_stage_name = models.CharField(
        max_length=300, verbose_name="Educational stage name"
    )
    edu_stage_name_as_slug = models.SlugField(
        verbose_name="Keep it empty", blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=("Created at"))

    class Meta:
        verbose_name = "Educational Stage"
        verbose_name_plural = "Educational Stages"

    def __str__(self):
        return self.edu_stage_name

    def save(self, *args, **kwargs):
        self.edu_stage_name_as_slug = slugify(self.edu_stage_name)
        super(EducationlStage, self).save(*args, **kwargs)


class EducationStageLevel(models.Model):
    related_edu_stage = models.ForeignKey(
        EducationlStage, on_delete=models.CASCADE, verbose_name="Related Edu Stage"
    )
    edu_stage_level = models.CharField(
        verbose_name="Educational Stage Level", max_length=350
    )
    edu_stage_level_as_slug = models.SlugField(
        verbose_name="Keep It empty", null=True, blank=True
    )
    created_At = models.DateTimeField(verbose_name="Created at", auto_now_add=True)

    def __str__(self):
        return self.edu_stage_level

    def save(self, *args, **kwargs):
        self.edu_stage_level_as_slug = slugify(self.edu_stage_level)
        super(EducationStageLevel, self).save(*args, **kwargs)


class Subject(models.Model):
    related_edu_stage_level = models.ForeignKey(
        EducationStageLevel,
        on_delete=models.CASCADE,
        verbose_name="Related Edu Stage Level",
    )
    subject_name = models.CharField(verbose_name="Subject Name", max_length=350)
    subject_thumbnail = models.ImageField(default="subject-thumbnail.png",upload_to="Subjects_Thumbnails", verbose_name="Subject's Thumbnail")
    semester = models.CharField(verbose_name="Semester", max_length=350)
    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)

    def __str__(self):
        return f"{self.subject_name}"