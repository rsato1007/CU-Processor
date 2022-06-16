# This file handles all serializers(transformation of python data to JSON data) done in the API.
# Documentation on serialization can be found here: https://www.django-rest-framework.org/api-guide/serializers/
from rest_framework import serializers
from .models import Member

# Documentation on model serializers can be found here: https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
# This class takes python data for members and transforms it into JSON data that the frontend can use.
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = [
            'first_name', 
            'last_name', 
            'middle_name',
            'prefix',
            'suffix',
            'pronouns',
            'verbal_password',
            'ssn',
            'date_of_birth',
            'date_of_death',
            'join_date',
            'address',
            'city',
            'state',
            'zip_code',
            'email',
            'home_number',
            'mobile_number',
            'work_number',
        ]