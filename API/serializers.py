from rest_framework import serializers

from Applications import models


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Application
        fields = "__all__"
