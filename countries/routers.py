from rest_framework import routers

from countries.views import CountriesViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'', CountriesViewSet)
