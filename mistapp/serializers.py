from rest_framework import serializers
from .models import Sorev


class SorevSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sorev
        fields = ('id',
                  'name',
                  'descriptions',
                  'members',
                  'result',
                  )
