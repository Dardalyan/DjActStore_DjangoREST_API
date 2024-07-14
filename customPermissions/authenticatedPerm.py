import jwt
from django.conf import settings

from rest_framework.permissions import BasePermission

from controller.jwt.JWTauthentication import JWTAuthentication
from model.user.models import User


class IsAuthenticatedByJWT(BasePermission):

    def has_permission(self, request, view):
        try:
            if request.user is not None and request.auth is not None:
                return True
            else: raise Exception('User is not authenticated !')
        except Exception as e:
            print(e)
            return False

