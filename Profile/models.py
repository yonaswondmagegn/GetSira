from typing import Iterable, Optional
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.validators import FileExtensionValidator

user = settings.AUTH_USER_MODEL

class Skill(models.Model):
    name = models.CharField(max_length=100)


class Profile(models.Model):
    usertype = (("E","EMPLOYER"),
                ("R","RECRUITER"))
    user_condition  = (("E","EMPLOED"),
                       ("UE","UNEMPLOED"))
    
    user = models.OneToOneField(user,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics',default="default.jpg")
    usertype = models.CharField(choices=usertype,max_length=1,default="E")
    short_desc = models.CharField(max_length=25,null=True,blank=True)
    skills = models.ForeignKey(Skill,on_delete=models.PROTECT,null=True,blank=True)
    self_desc = models.TextField(null=True,blank=True)
    portfolio = models.CharField(max_length=225,null=True,blank=True)
    cv = models.FileField(upload_to='cv',validators=[FileExtensionValidator(["PDF","docx"])],null=True,blank=True)
    user_condition = models.CharField(choices=user_condition,max_length=2,default="UE")
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(default= timezone.now)
    updated_date = models.DateTimeField(null=True,blank=True)


    def save(self,*args,**kwargs):
        self.updated_date = timezone.now()
        return super().save(*args,**kwargs)
 