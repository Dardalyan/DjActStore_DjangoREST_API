from .listing import ListAddresses
from django.urls import path

from .remove import RemoveAddresses
from .update import UpdateAddresses

urlpatterns = [
    path('address/<int:address_id>', ListAddresses.as_view()),
    path('address', ListAddresses.as_view()),
    path('address/update/<int:address_id>', UpdateAddresses.as_view()),
    path('address/remove/<int:address_id>', RemoveAddresses.as_view()),

]