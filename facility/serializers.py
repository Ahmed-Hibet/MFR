from rest_framework import serializers
from facility.models import Facility


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = [
            'id', 'name', 'email', 'number_of_medical_doctor', 
            'number_of_nurse', 'number_of_midwife', 'facility_types', 
            'status'
            ]
