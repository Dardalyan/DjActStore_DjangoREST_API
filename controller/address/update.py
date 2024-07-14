from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from controller.jwt.JWTauthentication import JWTAuthentication
from customPermissions.authenticatedPerm import IsAuthenticatedByJWT
from model.address.models import Address


class UpdateAddresses(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedByJWT,)

    def put(self, request, **kwargs):
        address_id = kwargs.get('address_id')
        current_user = request.user
        new_data = request.data

        try:

            if address_id is None:
                raise Exception('Address is None !')

            address = Address.objects.filter(id=address_id).first()

            for instance_key in address.__dict__.keys():
                for key in new_data.keys():
                    if key == instance_key:
                        address.__dict__[key] = new_data[key]
            address.save()

            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'error': 'Bad Request !'}, status=status.HTTP_400_BAD_REQUEST)