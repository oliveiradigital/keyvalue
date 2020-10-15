from django.urls import path
from .views import CreateUser


urlpatterns = [
    path('user', CreateUser.as_view(), name='accounts-create-user'),
]