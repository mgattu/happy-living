from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers

from .models import HUser
from .permissions import IsHUserOwner
from .serializers import HUserRegisterSerializer,HUserUpdateSerializer


class HUserViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = HUser.objects.all()
    serializer_class = HUserRegisterSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        if self.request.method == 'DELETE':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsHUserOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            HUser.objects.create_user(**serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        print serializer.errors

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def update(self, request, id=None):
    #     print request
    #     print "id is {}".format(id)

    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         print "valid"
    #         return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
    #     print serializer.errors
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HUserEditViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = HUser.objects.all()
    serializer_class = HUserUpdateSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        if self.request.method == 'PUT':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsHUserOwner(),)

