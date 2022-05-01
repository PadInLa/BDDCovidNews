from rest_framework import serializers

from graphs.models import CovidCasesCountry, CovidCasesDaily
import calendar


class CovidCasesCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CovidCasesCountry
        fields = ('country_region', 'confirmed', 'deaths', 'recovered', 'active',
                  'new_cases', 'new_deaths', 'new_recovered', 'deaths_100cases',
                  'recovered_100cases', 'deaths_100recovered', 'confirmed_lastweek',
                  'oneweek_change', 'oneweek_percincrease', 'region')


class CovidCasesDailyMonthlySerializer(serializers.Serializer):
    month = serializers.CharField()
    total_deaths = serializers.IntegerField()
    total_recovered = serializers.IntegerField()
    total_active = serializers.IntegerField()
    total_confirmed = serializers.IntegerField()

    def to_representation(self, instance):
        instance['month'] = calendar.month_name[instance['month']]
        return super().to_representation(instance)

class CovidCasesDailyNewMonthlySerializer(serializers.Serializer):
    month = serializers.CharField()
    new_cases = serializers.IntegerField()
    new_deaths = serializers.IntegerField()
    new_recovered = serializers.IntegerField()

    def to_representation(self, instance):
        instance['month'] = calendar.month_name[instance['month']]
        return super().to_representation(instance)

class CovidCasesDailyPerHundredMonthlySerializer(serializers.Serializer):
    month = serializers.CharField()
    deaths_100cases = serializers.FloatField()
    recovered_100cases = serializers.FloatField()
    deaths_100recovered = serializers.FloatField()

    def to_representation(self, instance):
        instance['month'] = calendar.month_name[instance['month']]
        return super().to_representation(instance)

class CovidCasesCountryCurrentSerializer(serializers.Serializer):
    region = serializers.CharField()
    region_deaths = serializers.IntegerField()
    region_recovered = serializers.IntegerField()
    region_confirmed = serializers.IntegerField()
    region_active = serializers.IntegerField()

class CovidCasesCountryNewSerializer(serializers.Serializer):
    region = serializers.CharField()
    new_cases = serializers.IntegerField()
    new_deaths = serializers.IntegerField()
    new_recovered = serializers.IntegerField() 

class CovidCasesCountryHundredSerializer(serializers.Serializer):
    region = serializers.CharField()
    deaths_100cases = serializers.FloatField()
    recovered_100cases = serializers.FloatField()
    deaths_100recovered = serializers.FloatField() 

class CovidCasesDailySerializer(serializers.ModelSerializer):
    class Meta:
        model = CovidCasesDaily
        fields = ('date', 'confirmed', 'deaths', 'recovered', 'active',
                  'new_cases', 'new_deaths', 'new_recovered', 'deaths_100cases',
                  'recovered_100cases', 'deaths_100recovered', 'num_countries')
