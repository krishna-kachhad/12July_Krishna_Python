from rest_framework import serializers
from .models import *


class cmtserializers(serializers.ModelSerializer):
    class Meta:
        model=comment
        fields='__all__'