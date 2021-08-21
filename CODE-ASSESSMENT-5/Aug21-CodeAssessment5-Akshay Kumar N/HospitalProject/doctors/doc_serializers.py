from rest_framework import serializers
from doctors.models import Doctor

class DoctorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('dcode','name','address','speciality','username','password')