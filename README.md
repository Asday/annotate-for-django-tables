# Annotate a QuerySet for use in django tables

This repo was produced as an answer to [this question](https://stackoverflow.com/questions/48500712/django-filter-and-django-tables2-using-a-foreign-attribute) on stack overflow.

## Installation

```shell
git clone git@github.com:Asday/annotate-for-django-tables.git
cd annotate-for-django-tables
mkvirtualenv --python=$(which python3.6) annotate-for-django-tables
python manage.py migrate
python manage.py shell
```

Within the django shell:

```python
from students.utils import create_dummy_data
create_dummy_data()  # This will take a minute or so.
exit()
```

Finally

```shell
python manage.py runserver 0.0.0.0:8000
```

Then visit [/students/](http://127.0.0.1:8000/students/).
