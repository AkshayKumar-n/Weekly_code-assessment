from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

# Create your views here.


@csrf_exempt

def addStudent(request):
    if(request.method == "POST"):
        getstudname = request.POST.get("Student Name")
        getadmno = request.POST.get("Admission no")
        getrollno = request.POST.get("Roll no")
        getclg = request.POST.get("College")
        getparentname = request.POST.get("Parent name")
        
        
        dict2 = {"Student Name":getstudname,"Admission":getadmno,"Roll no":getrollno,"College":getclg,"Parent Name":getparentname}
        result2 = json.dumps(dict2)
        return HttpResponse(result2)

    else:
        return HttpResponse("GET method not allowed") 
