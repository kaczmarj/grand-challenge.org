from django.conf.urls import url

from participants.views import (
    RegistrationRequestList,
    RegistrationRequestCreate,
    RegistrationRequestUpdate,
    ParticipantsList,
)

urlpatterns = [
    url(r'^$', ParticipantsList.as_view(), name='list'),
    url(
        r'^registration/$',
        RegistrationRequestList.as_view(),
        name='registration-list',
    ),
    url(
        r'^registration/create/$',
        RegistrationRequestCreate.as_view(),
        name='registration-create',
    ),
    url(
        r'^registration/(?P<pk>\d+)/update/$',
        RegistrationRequestUpdate.as_view(),
        name='registration-update',
    ),
]
