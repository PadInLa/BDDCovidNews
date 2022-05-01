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

    def to_representation(self, instance):
        instance['month'] = calendar.month_name[instance['month']]
        return super().to_representation(instance)


class CovidCasesDailySerializer(serializers.ModelSerializer):
    class Meta:
        model = CovidCasesDaily
        fields = ('date', 'confirmed', 'deaths', 'recovered', 'active',
                  'new_cases', 'new_deaths', 'new_recovered', 'deaths_100cases',
                  'recovered_100cases', 'deaths_100recovered', 'num_countries')
