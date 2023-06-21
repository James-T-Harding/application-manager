from django.urls import path, include
from rest_framework import routers

from API.views import ApplicationsViewSet

router = routers.DefaultRouter()
router.register(r'applications', ApplicationsViewSet)

urlpatterns = [
    path("", include(router.urls))
]