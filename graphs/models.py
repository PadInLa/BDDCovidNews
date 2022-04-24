from django.db import models

class CovidCasesCountry(models.Model):
    country_region = models.CharField(max_length=100)
    confirmed = models.IntegerField()
    deaths = models.IntegerField()
    recovered = models.IntegerField()
    active = models.IntegerField()
    new_cases = models.IntegerField()
    new_deaths = models.IntegerField()
    new_recovered = models.IntegerField()
    deaths_100cases = models.FloatField() 
    recovered_100cases = models.FloatField()
    deaths_100recovered = models.FloatField()
    confirmed_lastweek = models.IntegerField()
    oneweek_change = models.IntegerField()
    oneweek_percincrease = models.FloatField()
    region = models.CharField(max_length=100)

class CovidCasesDaily(models.Model):
    date = models.DateField()
    confirmed = models.IntegerField()
    deaths = models.IntegerField()
    recovered = models.IntegerField()
    active = models.IntegerField()
    new_cases = models.IntegerField()	
    new_deaths = models.IntegerField()
    new_recovered = models.IntegerField()	
    deaths_100cases = models.FloatField()
    recovered_100cases = models.FloatField()
    deaths_100recovered = models.FloatField()
    num_countries = models.IntegerField()

