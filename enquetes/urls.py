from django.urls import path
from enquetes.views import enquetes

urlpatterns = [
    path("", enquetes, name="enquetes")
]