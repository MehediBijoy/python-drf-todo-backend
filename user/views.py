from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import *


class loginAPI(APIView):
    def post(self, request):
        serializer = loginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = RefreshToken.for_user(user)
        return Response({
            'user': userSerializer(user).data,
            'access_token': str(token.access_token),
            'refresh_token': str(token)
        })


class registerAPI(APIView):
    def post(self, request):
        serializer = registerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        return Response({
            'user': serializer.data,
            'access_token': str(token.access_token),
            'refresh_token': str(token)
        })


class userAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = request.user
        return Response({
            'user': userSerializer(user).data
        })
