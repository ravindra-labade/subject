from django.db import models


class Subject(models.Model):
    subject_name = models.CharField(max_length=10)
    subject_teacher = models.CharField(max_length=20)
    total_students = models.IntegerField()
    subject_fee = models.IntegerField()


