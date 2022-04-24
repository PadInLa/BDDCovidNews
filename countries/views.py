from django.shortcuts import render
from rest_framework.response import Response

from countries.models import Country
from countries.serializers import CountrySerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from graphs.models import CovidCasesDaily
from graphs.serializers import CovidCasesDailySerializer

# Create your views here.


class CountriesViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    @action(
        methods=['GET'],
        detail=False,
        url_path='most-trash-country',
        url_name='most-trash-country'
    )
    def most_trash_country(self, request):
        queryset = Country.objects.all()
        trashiest_country = get_object_or_404(queryset, name='9519')
        serializer = CountrySerializer(trashiest_country)

        return Response(serializer.data)

    @action(
        methods=['GET'],
        detail=False,
        url_path='most-trash-countries',
        url_name='most-trash-countries'
    )
    def most_trash_countries(self, request):
        queryset = Country.objects.all()
        serializer = CountrySerializer(queryset, many=True)
        return Response(serializer.data)

    @action(
        methods=['GET'],
        detail=False,
        url_path='covid-cases-daily',
        url_name='covid-cases-daily'
    )
    def covid_cases_daily(self, request):
        queryset = CovidCasesDaily.objects.all()
        serializer = CovidCasesDailySerializer(queryset, many=True)
        return Response(serializer.data)
