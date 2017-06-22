import pytest

from django.core.management import call_command


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata',
                     '../../comicmodels/fixtures/comic_initial_project.json')
        call_command('loaddata',
                     '../../comicmodels/fixtures/user_everyone.json')
