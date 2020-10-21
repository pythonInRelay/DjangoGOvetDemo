from rest_framework import serializers
from .models import URLData


class URLDATASerializers(serializers.ModelSerializer):
    class Meta:
        model = URLData
        field = '__all__'  # Every time data is taken from models serialize everything
