from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from patients.models import Patients
from patients.serializers import PatientSerializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

def patients(request):
    return render(request,'index.html')

@csrf_exempt  
def addPatients(request):
    if(request.method == "POST"):
        mydata = JSONParser().parse(request)
        patient_serializer = PatientSerializers(data = mydata)
        if(patient_serializer.is_valid()):
            patient_serializer.save()
            return JsonResponse(patient_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization")
    else:
        return HttpResponse("GET Method is not allowed")

@csrf_exempt
def viewAll(request):
    if(request.method == "GET"):
        patient = Patients.objects.all()
        patient_serializers = PatientSerializers(patient,many=True)
        return JsonResponse(patient_serializers.data, safe=False)

@csrf_exempt
def view(request,id):
    try:
        patient = Patients.objects.get(id = id)

        if(request.method == "GET"):
            patient_serializers = PatientSerializers(patient)
            return JsonResponse(patient_serializers.data, safe=False)

        if(request.method == "DELETE"):
            patient.delete()
            return JsonResponse("Patient records deleted")

        if(request.method == "PUT"):
            mydata =JSONParser().parse(request)
            patient_serializers = PatientSerializers(patient,data=mydata)
            if(patient_serializers.is_valid()):
                patient_serializers.save()
                return JsonResponse(patient_serializers.data,status=status.HTTP_200_OK)

    except Patients.DoesNotExist:
        return HttpResponse("Invalid Patients ID",status=status.HTTP_404_NOT_FOUND)   
         
@csrf_exempt
def viewpcode(request,pcode):
    try:
        patient = Patients.objects.get(pcode = pcode)
        if(request.method == "GET"):
            patient_serializers = PatientSerializers(patient)
            return JsonResponse(patient_serializers.data, safe=False)
    except Patients.DoesNotExist:
        return HttpResponse("Invalid Patients Code",status=status.HTTP_404_NOT_FOUND)


            
