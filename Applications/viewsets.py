from django.views.generic import TemplateView

from Applications.models import Application


class IndexViewSet(TemplateView):
    template_name = "index.html"

    @property
    def extra_context(self):
        return dict(applications=list(Application.objects.all()))


class ApplicationViewSet(TemplateView):
    template_name = "application.html"

    def get_context_data(self, application_id, **kwargs):
        return super().get_context_data(**kwargs) | dict(application=Application.objects.get(id=application_id))
