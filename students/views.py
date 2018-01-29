from django.views.generic import ListView

from .models import Student
from .tables import StudentTable


class StudentListView(ListView):
    model = Student

    def get_queryset(self):
        return super().get_queryset() \
            .with_academic_standings(2018, 'current_standing')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['table'] = StudentTable(context['student_list'])

        return context
