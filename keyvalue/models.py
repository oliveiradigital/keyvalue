from django.db import models
from django.contrib.auth import get_user_model


class Data(models.Model):
    key = models.CharField(max_length=255, verbose_name='Key')
    value = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)