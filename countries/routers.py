from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'countries', None)
