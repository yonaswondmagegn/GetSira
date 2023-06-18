from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .CustomPermitin import SafeOrCreatorOnly
from .serializer import SiraSerializer
from .models import Sira


class SiraViewSet(ModelViewSet):
    queryset = Sira.objects.all()
    serializer_class = SiraSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,SafeOrCreatorOnly]
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ["type","chategory"]
    search_fields = ["title","description","requirement"]
    order_fileds = ["componsation","updated_date","date"]