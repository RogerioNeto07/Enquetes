from django.urls import path
from geral.views import coreindex

urlpatterns = [
    path("", coreindex, name="coreindex")
]