from rest_framework import serializers

from .models import RoleModel, UserModel


class RoleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=RoleModel
        fields=['name']

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=UserModel
        fields=['photo','username','password','email','first_name','last_name','identification_document_type',
                'number_of_identification','nationality','birth_date']