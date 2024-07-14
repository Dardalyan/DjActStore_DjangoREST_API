from .listing import ListProducts
from django.urls import path

urlpatterns = [
    path('products/<int:id>/', ListProducts.as_view()),
    path('products/', ListProducts.as_view()),

]