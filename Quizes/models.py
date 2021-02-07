from django.db import models

from Subjects.models import Subject

# Create your models here.
class Question(models.Model):
    question_body_as_text = models.TextField(verbose_name = "Question body as a text")
    question_body_as_image = models.ImageField(verbose_name = "Question body as an image")
    created_at = models.DateTimeField(auto_now_add=True ,verbose_name ="Created at")

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

class Answer(models.Model):
    related_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_as_text = models.TextField(verbose_name ="Answer as a text" )
    answer_as_img = models.ImageField(verbose_name ="Answer as an image")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name ="Created at") 

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"

class Quiz(models.Model):
    related_subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Related subject")
    related_questions = models.ManyToManyField(Question, verbose_name = "Related quetions")
    quiz_duration = models.CharField(max_length=300, verbose_name ="Quiz duration")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name ="Created at")

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizes"