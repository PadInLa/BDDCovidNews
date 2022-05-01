from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from django.db.models import Sum

from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models.functions import ExtractMonth
from graphs.models import CovidCasesCountry, CovidCasesDaily
from graphs.serializers import CovidCasesCountryCurrentSerializer, CovidCasesCountryHundredSerializer, CovidCasesCountryNewSerializer, CovidCasesCountrySerializer, CovidCasesDailyMonthlySerializer, CovidCasesDailyNewMonthlySerializer, CovidCasesDailyPerHundredMonthlySerializer, CovidCasesDailySerializer


class GraphViewSet(viewsets.ModelViewSet):
    queryset = CovidCasesDaily.objects.all()
    # Aquí solo puede declararle un serializador al ViewSet
    # y la variable se tiene que llamar serializer_class.
    # Tenga cuidado porque si no lo pone, no va a funcionar.
    # Tenga cuidado con hacer clases que respondan a librerías
    # de terceros porque tiene que nombrar las variables igual,
    # por lo que por detrás se convierte en un objeto y la librería
    # intenta buscar el atributo que le está definiendo aquí.
    # En realidad, debería hacer un ViewSet por cada modelo y asignarle
    # el serializador de ese modelo.
    # Nombre cosas que respondan a sus modelos, no a lo que vaya
    # a hacer con ellos en el front. Backend no sabe que usted va a usar
    # la información para hacer una gráfica, solo que tiene que enviar la info.
    Daily_serializer = CovidCasesDailySerializer
    Country_serializer = CovidCasesCountrySerializer

    @action(
        methods=['GET'],
        detail=False,
        url_path='covid-monthly-deaths',
        url_name='covid-monthly-deaths'
    )
    def covid_monthly_deaths(self, request):
        queryset = CovidCasesDaily.objects.all().annotate(
            month=ExtractMonth('date')
        ).values('month').annotate(
            total_deaths=Sum('deaths'),
            total_recovered=Sum('recovered'),
            total_active=Sum('active'), 
            total_confirmed=Sum('confirmed')).values(
                'month', 'total_deaths', 'total_recovered', 'total_active', 'total_confirmed'
                ).order_by('month')

        serializer = CovidCasesDailyMonthlySerializer(queryset, many=True)
        return Response(serializer.data)


    @action(
        methods=['GET'],
        detail=False,
        url_path='covid-monthly-newdata',
        url_name='covid-monthly-newdata'
    )
    def covid_monthly_newdata(self, request):
        queryset = CovidCasesDaily.objects.all().annotate(
            month=ExtractMonth('date')
        ).values('month').annotate(
            new_cases=Sum('new_cases'),
            new_deaths=Sum('new_deaths'),
            new_recovered=Sum('new_recovered')).values(
                'month', 'new_cases', 'new_deaths', 'new_recovered').order_by('month')

        serializer = CovidCasesDailyNewMonthlySerializer(queryset, many=True)
        return Response(serializer.data)

    @action(
        methods=['GET'],
        detail=False,
        url_path='covid-monthly-perhundred',
        url_name='covid-monthly-perhundred'
    )
    def covid_monthly_perhundred(self, request):
        queryset = CovidCasesDaily.objects.all().annotate(
            month=ExtractMonth('date')
        ).values('month').annotate(
            deaths_100cases=Sum('deaths_100cases'),
            recovered_100cases=Sum('recovered_100cases'),
            deaths_100recovered=Sum('deaths_100recovered')).values(
                'month', 'deaths_100cases', 'recovered_100cases', 'deaths_100recovered').order_by('month')

        serializer = CovidCasesDailyPerHundredMonthlySerializer(queryset, many=True)
        return Response(serializer.data)

    # Este método no es necesario. Si se crea otro ViewSet,
    # se generan todos los métodos por defecto.
    # ¿Para qué instalamos DRF (Django Rest Framework)
    # si va a volver a hacer lo que la librería ya hace?
    # Use el decorador @action para crear un método que DRF
    # no pueda generar por su cuenta.
    @action(
        methods=['GET'],
        detail=False,
        url_path='covid-region-info',
        url_name='covid-region-info'
    )
    def covid_region_info(self, request):
        queryset1 = CovidCasesCountry.objects.values(
            'region'
            ).annotate(
                region_deaths=Sum('deaths'),
                region_recovered=Sum('recovered'),
                region_confirmed=Sum('confirmed'),
                region_active = Sum('active')
            ).order_by('region').values(
                'region', 'region_deaths', 'region_recovered', 'region_confirmed', 'region_active').order_by('region')
        serializer = CovidCasesCountryCurrentSerializer(queryset1, many=True)
        return Response(serializer.data)

    @action(
        methods=['GET'],
        detail=False,
        url_path='covid-region-newdata',
        url_name='covid-region-newdata'
    )
    def covid_region_newdata(self, request):
        queryset1 = CovidCasesCountry.objects.values(
            'region'
            ).annotate(
                new_cases=Sum('new_cases'),
                new_deaths=Sum('new_deaths'),
                new_recovered=Sum('new_recovered')
            ).order_by('region').values(
                'region', 'new_cases', 'new_deaths', 'new_recovered').order_by('region')
        serializer = CovidCasesCountryNewSerializer(queryset1, many=True)
        return Response(serializer.data)

    @action(
        methods=['GET'],
        detail=False,
        url_path='covid-region-perhundred',
        url_name='covid-region-perhundred'
    )
    def covid_region_perhundred(self, request):
        queryset1 = CovidCasesCountry.objects.values(
            'region'
            ).annotate(
                deaths_100cases=Sum('deaths_100cases'),
                recovered_100cases=Sum('recovered_100cases'),
                deaths_100recovered=Sum('deaths_100recovered')
            ).order_by('region').values(
                'region', 'deaths_100cases', 'recovered_100cases', 'deaths_100recovered').order_by('region')
        serializer = CovidCasesCountryHundredSerializer(queryset1, many=True)
        return Response(serializer.data)
