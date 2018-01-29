from django.views.generic import ListView

from .models import Student


class StudentListView(ListView):
    model = Student

    def get_queryset(self):
        return super().get_queryset() \
            .with_academic_standings(2018, 'current_standings')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['table'] = None  # TODO

        return context
