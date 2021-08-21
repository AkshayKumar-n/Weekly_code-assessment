from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from doctors.models import Doctor
from doctors.doc_serializers import DoctorSerializers

def doctors(request):
    return render(request,'index1.html')

def doclogin(request):
    return render(request,'doctorlogin.html')
@csrf_exempt
def addDoctor(request):
    if(request.method == "POST"):
        mydict = JSONParser().parse(request)
        doc_serializer = DoctorSerializers(data = mydict)
        if(doc_serializer.is_valid()):
            doc_serializer.save()
            return JsonResponse(doc_serializer.data)
        else:
            return HttpResponse("Error in Serialization")
    else:
        return HttpResponse("GET method not allowed")

def viewAll(request):
    if(request.method == "GET"):
        doctor = Doctor.objects.all()
        doc_serializer = DoctorSerializers(doctor, many=True)
        return JsonResponse(doc_serializer.data, safe=False)
@csrf_exempt
def view(request,id):
    try:
        doctor = Doctor.objects.get(id = id )
        if(request.method == "GET"):
            doc_serializer = DoctorSerializers(doctor)
            return JsonResponse(doc_serializer.data, safe=False)

        if(request.method == "DELETE"):
            doctor.delete()
            return HttpResponse("Doctor's record Delete")

        if(request.method == "PUT"):
            mydict = JSONParser().parse(request)
            doc_serialize = DoctorSerializers(doctor, data = mydict)
            if(doc_serialize.is_valid()):
                doc_serialize.save()
                return JsonResponse(doc_serialize.data, status = status.HTTP_200_OK)
    except Doctor.DoesNotExist:
        return HttpResponse("Invalid Doctor ID",status=status.HTTP_404_NOT_FOUND)

def viewdcode(request,dcode):
    try:
        doctor = Doctor.objects.get(dcode = dcode)
        if(request.method == "GET"):
            doc_serializer = DoctorSerializers(doctor)
            return JsonResponse(doc_serializer.data, safe=False)
    except Doctor.DoesNotExist:
        return HttpResponse("Inavlid Doctor code",status=status.HTTP_404_NOT_FOUND)            
