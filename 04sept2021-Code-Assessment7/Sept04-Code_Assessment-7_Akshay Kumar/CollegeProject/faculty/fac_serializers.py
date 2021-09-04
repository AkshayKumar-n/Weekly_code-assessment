from rest_framework import serializers
from faculty.models import Faculty

class FacultySerializers(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('id','fcode','password','dept','name','address','mobno') 