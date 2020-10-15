from django.urls import path
from .views import KeyValue


urlpatterns = [
    path('data/<key>', KeyValue.as_view(), name='keyvalue-data')
]