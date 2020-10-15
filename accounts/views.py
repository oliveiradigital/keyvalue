from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


class CreateUser(APIView):
    def post(self, request):
        """Create a user and return the token."""
        username = get_random_string(length=20)
        password = get_random_string(length=20)
        email = '{}@localhost'.format(username)

        User = get_user_model()
        user = User.objects.create(username=username, password=password, email=email)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'success': True, 'token': token.key})
    