from django.db.models import Q
from django.views import generic

from Applications.models import Application


class SearchViewSet(generic.ListView):
    search_fields = []
    comparison_type = "icontains"

    def get_queryset(self):
        queryset = super().get_queryset()

        if search := self.request.GET.get("search"):
            queryset = queryset.filter(*map(self.contained_in_fields, search.split()))

        return queryset

    def contained_in_fields(self, term):
        result = Q()

        for field in self.search_fields:
            field += f"__{self.comparison_type}"
            result |= Q(**{field: term})

        return result


class IndexViewSet(SearchViewSet):
    template_name = "index.html"
    context_object_name = "applications"
    queryset = Application.objects.all()
    search_fields = ["job_title", "company_name"]

    @property
    def extra_context(self):
        return dict(search=self.request.GET.get("search", ""))


class ApplicationViewSet(generic.DetailView):
    model = Application
    template_name = "update_application.html"


class ApplicationCreateViewSet(generic.TemplateView):
    template_name = "new_application.html"
