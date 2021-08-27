from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from flats.serializers import FlatSerializer
import json
from flats.models import Flat
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
@csrf_exempt
def flataddpage(request):
    if(request.method =="POST"):
        getBuildNo=int(request.POST.get("BuildingNo"))
        getName=request.POST.get("OwnerName")
        getAddress=request.POST.get("Address")
        getMobileNo=request.POST.get("MobileNumber")
        getAadhaar=request.POST.get("AadhaarNumber")
        getEmailId=request.POST.get("EmailId")
        getPassword=request.POST.get("Password")
        mydict={"BuildingNo":getBuildNo,"OwnerName":getName,"Address":getAddress,"MobileNumber":getMobileNo,'AadhaarNumber':getAadhaar,'EmailId':getEmailId,'Password':getPassword}
        flat_serialize=FlatSerializer(data=mydict)
        if (flat_serialize.is_valid()):
            flat_serialize.save()
            return JsonResponse(flat_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialisation",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("No get method is allowed",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def searchapi(request):
    try:
        getBuildNo=int(request.POST.get("BuildingNo"))
        getFlat=Flat.objects.filter(BuildingNo=getBuildNo)
        flat_serializer=FlatSerializer(getFlat,many=True)
        return render(request,"search.html",{"data":flat_serializer.data})
    except Flat.DoesNotExist:
        return HttpResponse("Invalid data",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("invalid")

@csrf_exempt
def flat_list(request):
    if (request.method=="GET"):
        flats=Flat.objects.all()
        flat_serializer=FlatSerializer(flats,many=True)
        return JsonResponse(flat_serializer.data,safe=False)
@csrf_exempt
def flat_details(request,fetchid):
    try:
        flats=Flat.objects.get(id=fetchid)
    except Flat.DoesNotExist:
        return HttpResponse("Invalid id",status=status.HTTP_404_NOT_FOUND)
    if (request.method=="GET"):
        flat_serializer=FlatSerializer(flats)
        return JsonResponse(flat_serializer.data,safe=False)
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        flat_serialize=FlatSerializer(flats,data=mydict)
        if (flat_serialize.is_valid()):
            flat_serialize.save()
            return JsonResponse(flat_serialize.data,status=status.HTTP_200_OK)
        else:
            return JsonResponse(flat_serialize.errors,status=status.HTTP_400_BAD_REQUEST)

    if(request.method=="DELETE"):
        flats.delete()
        return HttpResponse("Deleted",status=status.HTTP_404_NOT_FOUND)


def flat_view(request):
    return render(request,'index.html')

def fl_view(request):
    fetchdata=requests.get("http://localhost:8000/flat/viewall/").json()
    return render(request,'viewall.html',{"data":fetchdata})

def search_view(request):
    return render(request,'search.html')

def upd_view(request):
    return render(request,'update.html')


@csrf_exempt
def updatesearchapi(request):
    try:
        getBuildNo=int(request.POST.get("BuildingNo"))
        getFlat=Flat.objects.filter(BuildingNo=getBuildNo)
        flat_serializer=FlatSerializer(getFlat,many=True)
        return render(request,'update.html',{"data":flat_serializer.data})
    except Flat.DoesNotExist:
        return HttpResponse("Invalid data",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("invalid")


@csrf_exempt
def update_data_read(request):
    getBuildingNo=int(request.POST.get("newBuildingNo"))
    getOwnerName=request.POST.get("newOwnerName")
    getid=request.POST.get("newid")
    getAddress=request.POST.get("newAddress")
    getMobileNumber=request.POST.get("newMobileNumber")
    getAadhaarNumber=request.POST.get("newAadhaarNumber")
    getEmailId=request.POST.get("newEmailId")
    getPassword=request.POST.get("newPassword")
    mydata={'BuildingNo':getBuildingNo,'OwnerName':getOwnerName,'Address':getAddress,'MobileNumber':getMobileNumber,'AadhaarNumber':getAadhaarNumber,'EmailId':getEmailId,'Password':getPassword}
    jsondata=json.dumps(mydata)
    Apilink="http://localhost:8000/flat/viewflats/" + getid
    print(jsondata)
    requests.put(Apilink,data=jsondata)
    return HttpResponse("data updated successfully")




@csrf_exempt
def delete_data_read(request):
    getnewid=request.POST.get("newid")
   
    Apilink="http://localhost:8000/flat/viewflats/" + getnewid
    requests.delete(Apilink)
    return HttpResponse("data deleted successfully")


@csrf_exempt
def deletesearchapi(request):
    try:
        getBuildNo=request.POST.get("BuildingNo")
        getFlat=Flat.objects.filter(BuildingNo=getBuildNo)
        flat_serializer=FlatSerializer(getFlat,many=True)
        return render(request,"delete.html",{"data":flat_serializer.data})
       
        return HttpResponse("Invalid data",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("invalid")

def del_view(request):
    return render(request,'delete.html')




