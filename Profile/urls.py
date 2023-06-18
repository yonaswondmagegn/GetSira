from django.urls import path 
from rest_framework_nested import routers
from .views import ProfileViewset,UserView


router = routers.DefaultRouter()
router.register('',ProfileViewset)
router.register('user',UserView)

urlpatterns = router.urls