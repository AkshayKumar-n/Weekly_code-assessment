
from rest_framework import serializers
from bloodbank.models import Donors

class DonorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Donors
        fields = ('id','name','address','bgroup','mobno','username','password')