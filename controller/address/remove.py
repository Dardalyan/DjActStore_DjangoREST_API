from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from controller.jwt.JWTauthentication import JWTAuthentication
from customPermissions.authenticatedPerm import IsAuthenticatedByJWT
from model.address.models import Address


class RemoveAddresses(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedByJWT,)

    def delete(self, request, **kwargs):
        address_id = kwargs.get('address_id')
        current_user = request.user

        try:

            if address_id is None:
                raise Exception('Address is None !')

            address = Address.objects.filter(id=address_id).first()
            current_user.addresses.remove(address)
            current_user.save()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'error': 'Bad Request !'}, status=status.HTTP_400_BAD_REQUEST)
