from django.urls import reverse
from django.views.generic import TemplateView

from Applications.models import Application


class IndexViewSet(TemplateView):
    template_name = "index.html"

    @property
    def extra_context(self):
        return dict(applications=list(Application.objects.all()))


class ApplicationViewSet(TemplateView):
    template_name = "update_application.html"

    def get_context_data(self, application_id, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data.update(application=Application.objects.get(id=application_id))

        return context_data


class ApplicationCreateViewSet(TemplateView):
    template_name = "new_application.html"
