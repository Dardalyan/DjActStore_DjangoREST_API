from .JWTview import JWTView
from django.urls import path

urlpatterns = [
    path('jwt-token/',JWTView.as_view(), name='jwt_token')
]