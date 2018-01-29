from datetime import date
from random import randint


def create_dummy_data():
    students = [Student.objects.create() for _ in range(30)]

    for student in students:
        for year in range(2012, 2018 + 1):
            AcademicStanding.objects.create(
                student=student,
                standing=randint(1, 10),
                year=date(year, 1, 1),
            )
