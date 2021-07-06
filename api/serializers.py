from reviewapp.models import Company,User,Review
from rest_framework import serializers
from django.shortcuts import get_object_or_404

class CompanySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Company
        fields = ["id","company_name","founder","description","date","averageRating","image"]
    
    def post(self):
        Company.objects.create(**self.validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","first_name","last_name","email"]

class ReviewSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    user = UserSerializer()
    class Meta:
        model = Review
        fields = "__all__"