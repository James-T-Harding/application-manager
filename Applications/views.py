from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from .models import Application


def update_application(request, application_id):
    application = get_object_or_404(Application, id=application_id)

    for item in request.POST.items():
        setattr(application, *item)

    application.save()
    return HttpResponseRedirect("/")


def create_application(request):
    data = dict(request.POST.items())
    del data["csrfmiddlewaretoken"]

    Application.objects.create(**data)

    return HttpResponseRedirect("/")