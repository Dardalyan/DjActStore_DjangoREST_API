from .process import PaymentProcess
from django.urls import path

urlpatterns = [
    path('process/payment', PaymentProcess.as_view()),
]