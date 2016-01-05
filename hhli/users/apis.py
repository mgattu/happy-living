# from django.conf.urls import url, include
# from .models import Customer
# from rest_framework import routers
# from rest_framework import serializers
# from rest_framework import viewsets

# # Serializers define the API representation.
# class CustomerSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Customer
#         fields = ('email', 'first_name', 'middle_name', 'last_name')

# # ViewSets define the view behavior.
# class CustomerViewSet(viewsets.ModelViewSet):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer

# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', CustomerViewSet)