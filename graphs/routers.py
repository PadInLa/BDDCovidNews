from rest_framework import routers

from graphs.views import GraphViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'', GraphViewSet)