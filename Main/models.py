from typing import Iterable, Optional
from django.db import models
from django.conf import settings
from Profile.models import Profile,Skill
from django.utils import timezone
from django.core.validators import FileExtensionValidator

user = settings.AUTH_USER_MODEL


class SiraType(models.Model):
    type_choise = (
        ("P","PERMANENT"),
        ("C","CONTRAT"),
        ("F","FREELANCING"),
        ("PE","PAID_INTERNSHIP"),
        ("UE","UNPAID_INTERNSHIP"),
    )
    type = models.CharField(choices=type_choise,max_length=3,default="P")


class SiraChategory(models.Model):
    title = models.CharField(max_length=50)

class Sira(models.Model):
    componsation_type = (("M","MONTHLY"),
                         ("H","HOURLY"),
                         ("F","FIXED_PRICE"))
    
    closed_reason = (
        ("G","GETIN GETSIRA"),
        ("US","UNSATISFAID"),
        ("OP","GETINOTHER PLACE"),
        ("O","GETINOTHERPLACE")
        )
    

    recruiter = models.ForeignKey(Profile,on_delete=models.PROTECT)
    type = models.ForeignKey(SiraType,on_delete=models.PROTECT)
    componsation_type = models.CharField(choices=componsation_type,max_length=1,default="M")
    componsation = models.IntegerField()
    componsation_range = models.IntegerField(null=True,blank=True)
    title = models.CharField(max_length=225)
    description = models.TextField()
    requirement = models.TextField()
    set_of_skills = models.ManyToManyField(Skill,related_name= "set_of_skills")
    chategory = models.ForeignKey(SiraChategory,on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    delete = models.BooleanField(default=False)
    closed_reason = models.CharField(choices=closed_reason,max_length=2,null=True,blank=True)
    date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)


class Aplication(models.Model):
    sira = models.ForeignKey(Sira,on_delete=models.PROTECT)
    applicant = models.ForeignKey(Profile,on_delete=models.PROTECT)
    coverletter = models.TextField()
    relatedworks = models.FileField(upload_to='related_works',validators=[FileExtensionValidator(["PDF","docx"])],null = True,blank=True)
    date =  models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(null= True)

    def save(self,*args,**kwargs):
        self.updated_date = timezone.now()
        return super().save(*args,**kwargs)