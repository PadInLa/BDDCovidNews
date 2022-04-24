from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from graphs.models import CovidCasesDaily


def index(request):
    dailys = CovidCasesDaily.objects.all().values('deaths')
    deaths_list = (list(dailys))
    deaths_dicts = dict()
    deaths_dicts['deaths'] = deaths_list
    return JsonResponse(deaths_dicts)
