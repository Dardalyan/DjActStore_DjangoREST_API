from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from model.product.models import Product

from ..jwt.JWTauthentication import JWTAuthentication
from customPermissions.authenticatedPerm import IsAuthenticatedByJWT


class PaymentProcess(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedByJWT,)

    def post(self, request):

        products = []
        try:
            payment_data = request.data.get('payment_data')
            product_data = request.data.get('product_data')
            current_user = request.user

            if payment_data or product_data or current_user is None:
                raise Exception('Information missing...')

            if len(payment_data['card_number']) != 16:
                raise Exception('Invalid card number !')

            for p in product_data:
                product = Product.objects.filter(product_id=p['product_id'])
                if product is None: raise Exception('Product not found!')
                products.append(product)

            for p in products:
                p.count -= 1
                p.save()
                current_user.order.products.add(p)
                current_user.save()

            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(data={'Payment unsuccessful !'}, status=status.HTTP_400_BAD_REQUEST)
