from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from controller.jwt.JWTauthentication import JWTAuthentication
from model.user.models import User
from serializers.userSerializer import UserSerializer


class JWTView(APIView):

    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user = User.objects.get(phone=request.data['phone'])
        password = request.data['password']

        if user is None or not user.check_password(password):
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        jwt_token = JWTAuthentication.create_jwt(user)

        return Response({'token': jwt_token})