from dataclasses import field
from rest_framework import serializers
from .models import Moment, Photo

class MomentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moment
        fields = ('id', 'title', 'description', 'user')

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'url', 'moment')