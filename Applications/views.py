from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from django.urls import reverse

from .models import Application


def update_application(request, application_id):
    application = get_object_or_404(Application, id=application_id)

    for item in request.POST.items():
        setattr(application, *item)

    application.save()
    return HttpResponseRedirect("/")
