from .listing import ListOrders
from django.urls import path

urlpatterns = [
    path('orders/<int:address_id>/', ListOrders.as_view()),
    path('orders/', ListOrders.as_view()),
]