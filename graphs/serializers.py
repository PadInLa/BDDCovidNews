from rest_framework import serializers

from graphs.models import CovidCasesCountry, CovidCasesDaily

class CovidCasesCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CovidCasesCountry
        fields = ('country_region','confirmed','deaths','recovered','active',
        'new_cases','new_deaths','new_recovered','deaths_100cases',
        'recovered_100cases','deaths_100recovered','confirmed_lastweek',
        'oneweek_change','oneweek_percincrease','region')

class CovidCasesDailySerializer(serializers.ModelSerializer):
    class Meta:
        model = CovidCasesDaily
        fields = ('date','confirmed','deaths','recovered','active',
        'new_cases','new_deaths','new_recovered','deaths_100cases',
        'recovered_100cases','deaths_100recovered','num_countries')
