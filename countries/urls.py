from django.conf.urls import url
from django.urls import include

from .routers import router

urlpatterns = [
    url(r'^', include(router.urls)),
]
