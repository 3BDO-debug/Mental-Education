from django.db import models

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(verbose_name="Subject Name", max_length=350)
    subject_code = models.CharField(verbose_name="Subject Code", max_length=350)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    def __str__(self):
        return self.subject_name
