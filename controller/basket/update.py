from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from model.basket.models import Basket
from model.product.models import Product
from serializers.basketSerializer import BasketSerializer
from ..jwt.JWTauthentication import JWTAuthentication
from customPermissions.authenticatedPerm import IsAuthenticatedByJWT


class UpdateBasket(APIView):

    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedByJWT,)

    def put(self, request, *args, **kwargs):
        product_id = kwargs['product_id']
        current_user = request.user

        try:
            if current_user.id is None:
                raise Exception('Authentication required !')

            basket = Basket.objects.filter(user=current_user).first()
            product = Product.objects.filter(product_id=product_id).first()

            if (product or basket) is None:
                raise Exception('Product or basket not found')

            if not product.count <= 0:
                product.basket.add(basket)
                product.count -= 1
                product.save()
            else:
                return Response(data={'There is no enough number of selected product !'},status=status.HTTP_406_NOT_ACCEPTABLE)

            single_or_list = BasketSerializer(basket)
            return Response(single_or_list.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'error': ' Bad Request !'}, status=status.HTTP_400_BAD_REQUEST)

