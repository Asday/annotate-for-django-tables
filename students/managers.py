from django.db import models


class StudentQuerySet(models.QuerySet):

    def with_academic_standings(self, year, field_name='academic_standings'):
        from .models import AcademicStanding  # Avoid circular import

        kwargs = {
            field_name: models.Subquery(
                AcademicStanding.objects.for_year(year).values('standing'),
            ),
        }
        return self.annotate(**kwargs)


StudentManager = models.Manager.from_queryset(StudentQuerySet)


class AcademicStandingQuerySet(models.QuerySet):

    def for_year(self, year):
        return self.filter(year__year=year)


AcademicStandingManager = models.Manager.from_queryset(AcademicStandingQuerySet)  # noqa
