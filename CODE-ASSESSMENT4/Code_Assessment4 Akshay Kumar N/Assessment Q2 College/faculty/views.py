from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

# Create your views here.

@csrf_exempt
def addFaculty(request):
    if(request.method == "POST"):
        getFacname = request.POST.get("Faculty Name")
        getFacadd = request.POST.get("Address")
        getFacDept = request.POST.get("Department")
        getFacCollege = request.POST.get("College")
        
        
        dict1 = {"Faculty Name":getFacname,"Address":getFacadd,"Department":getFacDept,"College":getFacCollege}
        result1 = json.dumps(dict1)
        return HttpResponse(result1)

    else:
        return HttpResponse("GET method not allowed")    




