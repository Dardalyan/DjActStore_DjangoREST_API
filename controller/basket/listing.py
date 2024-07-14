from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from model.basket.models import Basket
from serializers.basketSerializer import BasketSerializer
from ..jwt.JWTauthentication import JWTAuthentication
from customPermissions.authenticatedPerm import IsAuthenticatedByJWT


class ListBasket(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedByJWT,)

    def get(self, request, **kwargs):

        current_user = request.user
        try:
            if current_user is None:
                raise Exception('Authentication required !')
            basket = Basket.objects.filter(user=current_user).first()
            single_or_list = BasketSerializer(basket)
            return Response(single_or_list.data)
        except Exception as e :
            print(e)
            return Response({'error': ' Bad Request !'}, status=status.HTTP_400_BAD_REQUEST)
