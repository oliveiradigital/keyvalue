from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Data


class KeyValue(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, key=None):
        data = Data.objects.filter(user=request.user, key=key).first()
        if data:
            exists = True
            value = data.value
        else:
            exists = False
            value = None
        return Response({'success': True, 'exists': exists, 'value': value})

    def post(self, request, key=None):
        value = request.data.get('value', '')
        data = Data.objects.filter(user=request.user, key=key).first()
        if data:
            data.value = value
            data.save()
            created = False
        else:
            data = Data.objects.create(user=request.user, key=key, value=value)
            created = True
        return Response({'success': True, 'created': created, 'key': key, 'value': value})
