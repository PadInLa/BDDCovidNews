from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from graphs.models import CovidCasesCountry, CovidCasesDaily
from graphs.serializers import CovidCasesCountrySerializer, CovidCasesDailySerializer


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

    # Este método no es necesario. Ya viene por defecto.
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

    # Este método no es necesario. Si crea otro ViewSet,
    # se generan todos los métodos por defecto.
    # ¿Para qué instalamos DRF (Django Rest Framework)
    # si va a volver a hacer lo que la librería ya hace?
    # Use el decorador @action para crear un método que DRF
    # no pueda generar por su cuenta.
    @action(
        methods=['GET'],
        detail=False,
        url_path='covid-cases-country',
        url_name='covid-cases-country'
    )
    def covid_cases_country(self, request):
        queryset1 = CovidCasesCountry.objects.all()
        serializer = CovidCasesCountrySerializer(queryset1, many=True)
        return Response(serializer.data)


# def index(request):
#     date = CovidCasesDaily.objects.all().values('date')
#     confirmed = CovidCasesDaily.objects.all().values('confirmed')
#     deaths = CovidCasesDaily.objects.all().values('deaths')
#     recovered = CovidCasesDaily.objects.all().values('recovered')
#     active = CovidCasesDaily.objects.all().values('active')
#     new_cases = CovidCasesDaily.objects.all().values('new_cases')
#     new_deaths = CovidCasesDaily.objects.all().values('new_deaths')
#     new_recovered = CovidCasesDaily.objects.all().values('new_recovered')
#     deaths_100cases = CovidCasesDaily.objects.all().values('deaths_100cases')
#     recovered_100cases = CovidCasesDaily.objects.all().values('recovered_100cases')
#     deaths_100recovered = CovidCasesDaily.objects.all().values('deaths_100recovered')
#     num_countries = CovidCasesDaily.objects.all().values('num_countries')
#     daily_list = (list(dailys))
#     daily_dicts = dict()
#     daily_dicts['daily'] = daily_list
#     return JsonResponse(daily_dicts)
