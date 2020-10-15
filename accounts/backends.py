from django.contrib.auth.backends import BaseBackend


class OnlyTokenBackend(BaseBackend):
    def authenticate(self, request, token=None):
        pass

    def get_user(self, user_id):
        pass