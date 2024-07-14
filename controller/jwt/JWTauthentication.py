from datetime import timedelta, datetime

import jwt
from django.conf import settings
from model.user.models import User
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed, APIException


class JWTAuthentication(BaseAuthentication):

    def authenticate(self, request):
        jwt_token = request.META.get('HTTP_AUTHORIZATION')
        if jwt_token is None:
            raise AuthenticationFailed('Token is requested !')

        jwt_token = JWTAuthentication.get_the_token_from_header(jwt_token)
        try:
            payload = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=['HS256'])
        except:
            raise AuthenticationFailed('Invalid signature')

        id = payload.get('id')
        user = User.objects.filter(id=id).first()
        if user is not None:
            return user, jwt_token
        else:
            raise AuthenticationFailed('Requested user cannot be found !')


    def authenticate_header(self, request):
        return 'Bearer'

    @classmethod
    def create_jwt(cls, user: User):
        payload = {
            'id': user.id,
            'exp': int((datetime.now() + timedelta(hours=settings.JWT_CONF['TOKEN_LIFETIME_HOURS'])).timestamp()),
            'iat': datetime.now().timestamp(),
            'name': user.name,
            'surname': user.surname
        }

        jwt_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        return jwt_token

    @classmethod
    def get_the_token_from_header(cls, token):
        token = token.replace('Bearer', '').replace(' ', '')  # clean the token
        return token
