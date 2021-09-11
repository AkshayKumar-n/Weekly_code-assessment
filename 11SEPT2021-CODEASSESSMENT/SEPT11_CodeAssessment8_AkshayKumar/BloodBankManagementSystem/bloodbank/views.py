from bloodbank.serializers import DonorSerializers
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bloodbank.models import Donors
import requests,json
from rest_framework.parsers import JSONParser
from rest_framework import status

def registerDonor(request):
    return render(request,'register.html')

def home(request):
    return render(request,'home.html')
def login(request):
    return render(request, 'login.html')

def viewDonor(request):
    fetch = requests.get("http://127.0.0.1:8000/bloodbank/viewdonor/").json()

    return render(request,'view.html',{"data": fetch})

def updateDonor(request):
    return render(request,'update.html')


@csrf_exempt
def addDonor(request):
    if(request.method == "POST"):
       
        donor_s = DonorSerializers(data = request.POST)
        if(donor_s.is_valid()):
            donor_s.save()
            return JsonResponse(donor_s.data)
        else:
            return HttpResponse("Error in Serialization")
    else:
        return HttpResponse("GET Method not allowed")


@csrf_exempt
def login_check(request):
   
    try:
        username = request.POST.get("username")
        password = request.POST.get("password")

        getUser = Donors.objects.filter(username = username, password=password)
        d_serializer = DonorSerializers(getUser, many=True)
        if(d_serializer.data):
            for i in d_serializer.data:
                x = i["name"]
                print(x)
            request.session['uname'] = x
            return render(request, 'header.html')

        else:
            return HttpResponse("Invalid Credentials")

    except Donors.DoesNotExist:
        return HttpResponse("User not found")




@csrf_exempt
def viewAll(request):
    if(request.method == "GET"):
        user = Donors.objects.all()
        us_serializer = DonorSerializers(user, many=True)
        return JsonResponse(us_serializer.data, safe=False)

@csrf_exempt
def view(request,id):
    try:
        user = Donors.objects.get(id = id )
        if(request.method == "GET"):
            user_serializer = DonorSerializers(user)
            return JsonResponse(user_serializer.data, safe=False)

        

        if(request.method == "PUT"):
            mydict = JSONParser().parse(request)
            user_serialize = DonorSerializers(user, data = mydict)
            if(user_serialize.is_valid()):
                user_serialize.save()
                return JsonResponse(user_serialize.data, status = status.HTTP_200_OK)
    except Donors.DoesNotExist:
        return HttpResponse("Invalid user ID",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def update_search(request):
    try:
        getUsername = request.POST.get("name")
        getUser = Donors.objects.filter(name = getUsername )
        user_serializer = DonorSerializers(getUser, many=True)
        return render(request,'update.html',{"data":user_serializer.data}) 
    except:
        return HttpResponse("No Users found",status=status.HTTP_404_NOT_FOUND)




@csrf_exempt
def update_data(request):
    getnewid = request.POST.get("newid")
    getname = request.POST.get("newname")
    getaddress = request.POST.get("newaddress")
    getbgroup = request.POST.get("newbgroup")
    getmobno = request.POST.get("newmobno")
    getusername = request.POST.get("newusername")
    getpassword = request.POST.get("newpassword")
    
    mydata= {"name":getname,"address":getaddress,"bgroup":getbgroup,"mobno":getmobno,"username":getusername,"password":getpassword}
    jsondata = json.dumps(mydata)
    Apilink = "http://127.0.0.1:8000/users/view/"+getnewid
    requests.put(Apilink,data = jsondata)
    return HttpResponse("Data Updated Successfully")


