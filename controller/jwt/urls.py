from .JWTview import JWTView
from django.urls import path

urlpatterns = [
    path('login/',JWTView.as_view(), name='login')
]