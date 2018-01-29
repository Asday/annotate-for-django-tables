from django.db import models


class Student(models.Model):
    pass


class AcademicStanding(models.Model):
    student = models.ForeignKey(
        'students.Student',
        related_name='academic_standings',
        on_delete=models.CASCADE,
    )
    standing = models.PositiveIntegerField()
    year = models.DateField()
