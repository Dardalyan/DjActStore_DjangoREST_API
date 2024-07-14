from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from model.order.models import Order
from serializers.orderSerializer import OrderSerializer
from ..jwt.JWTauthentication import JWTAuthentication
from customPermissions.authenticatedPerm import IsAuthenticatedByJWT


class ListOrders(APIView):

    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedByJWT,)

    def get(self, request, **kwargs):

        order_id = kwargs.get('order_id')
        current_user = request.user

        try:

            if order_id is None:
                orders = current_user.order.all()
                serializer = OrderSerializer(orders, many=True)
                print(serializer.data)
                return Response(data=serializer.data, status=status.HTTP_200_OK)

            else:
                order = Order.objects.filter(id=order_id).first()
                serializer = OrderSerializer(order) 
                return Response(data=serializer.data, status=status.HTTP_200_OK)

        except Exception as e :
            print(e)
            return Response({'error': ' Bad Request !'}, status=status.HTTP_400_BAD_REQUEST)