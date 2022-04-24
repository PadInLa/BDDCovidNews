from rest_framework import serializers

from graphs.models import CovidCasesDaily


class CovidCasesDailySerializer(serializers.ModelSerializer):
    class Meta:
        model = CovidCasesDaily
        fields = ('id', 'deaths')
