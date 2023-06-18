from django.db.models.signals import post_save
from .models import Profile
from django.dispatch import receiver
from django.conf import settings

User = settings.AUTH_USER_MODEL


@receiver(post_save,sender = User)
def create_user(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user = instance)
