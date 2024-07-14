from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from model.product.models import Product
from serializers.productSerializer import ProductSerializer


class ListProducts(APIView):

    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)

    def get(self, request , **kwargs):
        single_or_list = None
        product_id = kwargs.get('id')

        try:
            if product_id is not None:
                single_or_list = ProductSerializer(Product.objects.get(product_id=product_id))
            if product_id is None:
                single_or_list = ProductSerializer(Product.objects.all(), many=True)
            return Response(single_or_list.data)
        except:
            return Response({'error': 'Bad Request !'}, status=status.HTTP_400_BAD_REQUEST)






