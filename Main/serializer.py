from rest_framework import serializers
from Profile.serializer import SkillSerializer
from .models import Sira,SiraChategory,Skill,SiraType,Aplication

class SiraChategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SiraChategory
        fields = "__all__"

class SiraTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiraType
        fields = "__all__"

class SiraSerializer(serializers.ModelSerializer):
    set_of_skills = SkillSerializer(many = True)
    chategory = SiraChategorySerializer()
    type = SiraTypeSerializer()

    class Meta:
        model = Sira
        fields = "__all__"