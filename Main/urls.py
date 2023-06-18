from django.urls import path
from rest_framework_nested import routers
from .views import SiraViewSet


route = routers.DefaultRouter()
route.register("sira",SiraViewSet)

urlpatterns = route.urls