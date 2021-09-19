from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import todoModel
from .serializers import todoSerializer


class TodoAPI(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]
    def get(self, request):
        queryset = todoModel.objects.all()
        serializer = todoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = todoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
    # def put(self, request):
    #     return Response()

    # def delete(self, request):
    #     return Response()
