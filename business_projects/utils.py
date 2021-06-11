from rest_framework import serializers

class ArrayOfCodesSerializer(serializers.ListField):
    child=serializers.CharField()

class ArrayOfNumberSerializer(serializers.ListField):
    child=serializers.IntegerField()