from .listing import ListBasket
from django.urls import path

from .remove import RemoveBasket
from .update import UpdateBasket

urlpatterns = [
    path('basket/', ListBasket.as_view()),
    path('basket/update/<int:product_id>', UpdateBasket.as_view()),
    path('basket/delete/<int:product_id>', RemoveBasket.as_view()),
 ]