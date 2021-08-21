from rest_framework import serializers
from patients.models import Patients

class PatientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = ('pcode','name','address','disease','admitstatus')