from django.shortcuts import render
from .models import Profile
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .serializer import ProfileSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from Main.CustomPermitin import SafeOrCreatorOnly
from rest_framework.viewsets import ModelViewSet
from django.conf import settings 
from core.models import User


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewset(ModelViewSet):
    queryset = Profile.objects.all()
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    fitlerset_fields = ["usertype","skills"]
    permission_classes = [IsAuthenticatedOrReadOnly,SafeOrCreatorOnly]
    search_fields = ["user__name","short_desc","self_desk","skills__name"]
    serializer_class = ProfileSerializer
