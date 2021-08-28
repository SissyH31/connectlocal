"""connectlocal URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from backend.models import Requests
from backend.models import Contacts
from backend.models import Users
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import include, path
from rest_framework import routers, serializers, viewsets, permissions
from django_filters import rest_framework as filters
from rest_framework import generics


# Serializers define the API representation.
class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


BUSINESS_CHOICES = (
    ('R', 'Restaurant'),
    ('F', 'Farm'),
)


class RequestFilter(filters.FilterSet):
    business_type = filters.ChoiceFilter(choices=BUSINESS_CHOICES)

    class Meta:
        model = Requests
        fields = ['business_type']


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Requests.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RequestSerializer
    filter_class = RequestFilter
    filterset_fields = ('business_type')


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ContactSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('requests', RequestViewSet, 'requests')
router.register('contacts', ContactViewSet, 'contacts')
router.register('users', UserViewSet, 'users')

urlpatterns = [
    path('', include('backend.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
