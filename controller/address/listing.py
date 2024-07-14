from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from model.address.models import Address
from model.user.models import User
from serializers.addressSerializer import AddressSerializer
from ..jwt.JWTauthentication import JWTAuthentication
from customPermissions.authenticatedPerm import IsAuthenticatedByJWT


class ListAddresses(APIView):

    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedByJWT,)

    def get(self, request, **kwargs):
        address_id = kwargs.get('address_id')
        current_user = request.user

        try:

            if address_id is None:
                addresses = current_user.addresses.all()
                serializer = AddressSerializer(addresses, many=True)
                print(serializer.data)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                address = Address.objects.filter(id=address_id).first()
                serializer = AddressSerializer(address)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'error': 'Bad Request !'}, status=status.HTTP_400_BAD_REQUEST)