from rest_framework import serializers
from .models import *


class bookserializers(serializers.ModelSerializer):
    class Meta:
        model=bookinfo
        fields='__all__'