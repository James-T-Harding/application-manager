from django.urls import path

from . import views, viewsets

app_name = "applications"
urlpatterns = [
    path("", viewsets.IndexViewSet.as_view()),
    path("<int:application_id>/", viewsets.ApplicationViewSet.as_view(), name="detail"),
    path("<int:application_id>/update", views.update_application, name="update"),
]