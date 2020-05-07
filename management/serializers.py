from rest_framework import serializers
from management.models import Example


class ExampleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Example
        fields = '__all__'