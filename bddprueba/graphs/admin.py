from django.contrib import admin
from graphs.models import CovidCasesCountry, CovidCasesDaily

@admin.register(CovidCasesCountry)
class CovidCasesCountryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
    )
@admin.register(CovidCasesDaily)
class CovidCasesDailyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
    )