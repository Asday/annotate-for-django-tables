from random import choice, randint

from django.db import models


vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'


def generate_name():
    length = randint(7, 20)
    name = []
    consonant = choice((True, False))
    for i in range(length):
        if consonant:
            name.append(choice(consonants))
        else:
            name.append(choice(vowels))

        consonant ^= True  # Flip to the opposite value.

    return ''.join(name)


class Student(models.Model):
    name = models.CharField(max_length=20, default=generate_name)

    def __str__(self):
        return self.name


class AcademicStanding(models.Model):
    student = models.ForeignKey(
        'students.Student',
        related_name='academic_standings',
        on_delete=models.CASCADE,
    )
    standing = models.PositiveIntegerField()
    year = models.DateField()
