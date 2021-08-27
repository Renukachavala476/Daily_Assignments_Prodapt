from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, request
from flats.serializers import FlatSerializer
from flats.models import Flat
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests, json

# Create your views here.

def home_page(request):
    return render(request,'home.html')

def add_flat(request):
    return render(request,'addflat.html')


def view_all(request):

    fetchdata=requests.get("http://127.0.0.1:8000/flats/viewallflats/").json()

    return render(request,'viewallflats.html',{"data":fetchdata})


def search_flat(request):
    return render(request,'searchflat.html')


def update_flat(request):
    return render(request,'updateflat.html')


def delete_flat(request):
    return render(request,'deleteflat.html')




@csrf_exempt 
def flatPage(request):
    if(request.method=="POST"):
        # flatsdict=JSONParser().parse(request)
        flats_serializer=FlatSerializer(data=request.POST)
        if(flats_serializer.is_valid()):
            flats_serializer.save()
            return JsonResponse(flats_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("No Get method allowed",status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def flats_list(request):
    if(request.method=="GET"):
        flats=Flat.objects.all()
        flats_serializer=FlatSerializer(flats,many=True)
        return JsonResponse(flats_serializer.data,safe=False)


@csrf_exempt
def flat_details(request,id):
    try:
        flats=Flat.objects.get(id=id)
        if(request.method =="GET"):
            flats_serializer=FlatSerializer(flats)
            return JsonResponse(flats_serializer.data,safe=False,status=status.HTTP_200_OK)

        if (request.method=="DELETE"):
            flats.delete()
            return HttpResponse("Deleted",status=status.HTTP_200_OK)
        if (request.method=="PUT"):
            flatsdict=JSONParser().parse(request)
            flats_serializer=FlatSerializer(flats,data=flatsdict)
            if(flats_serializer.is_valid()):
                flats_serializer.save()
                return JsonResponse(flats_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(flats_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Flat.DoesNotExist:
        return HttpResponse("invalid building number",status=status.HTTP_404_NOT_FOUND)



@csrf_exempt
def search_api(request):
    try:
        getBuildingNo = request.POST.get("building_no")
        getFlat = Flat.objects.filter(building_no=getBuildingNo)
        flats_serializer = FlatSerializer(getFlat, many=True)
        return render(request,"searchflat.html",{"data":flats_serializer.data})
        # return JsonResponse(train_serializer.data,safe=False, status=status.HTTP_200_OK)
    except Flat.DoesNotExist:
        return HttpResponse("Invalid Building number",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Error")


@csrf_exempt
def update_search_api(request):
    try:
        getBuildingNo = request.POST.get("building_no")
        getFlat = Flat.objects.filter(building_no=getBuildingNo)
        flats_serializer = FlatSerializer(getFlat, many=True)

        return render(request,"updateflat.html",{"data":flats_serializer.data})
        # return JsonResponse(train_serializer.data,safe=False, status=status.HTTP_200_OK)
    except Flat.DoesNotExist:
        return HttpResponse("Invalid Building number",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def update_data_read(request):
    getId = request.POST.get("newid")

    getBuildingno = request.POST.get("newbuilding_no")
    getOwnername = request.POST.get("newowner_name")
    getAddress = request.POST.get("newaddress")
    getMobileno = request.POST.get("newmobile_no")
    getAadharno = request.POST.get("newaadhar_no")
    getEmailid = request.POST.get("newemail")
    getPassword = request.POST.get("newpassword")

    mydata={'building_no':getBuildingno,'owner_name':getOwnername,'address':getAddress,'mobile_no':getMobileno,'aadhar_no':getAadharno,'email':getEmailid,'password':getPassword}
    jsondata=json.dumps(mydata)
    ApiLink="http://127.0.0.1:8000/flats/viewaflat/" + getId
    requests.put(ApiLink,data=jsondata)
    return HttpResponse("Data updated successfully")


@csrf_exempt
def delete_search_api(request):
    try:
        getBuildingno=request.POST.get("building_no")
        getBuildingnumber=Flat.objects.filter(building_no=getBuildingno)
        flats_serializer=FlatSerializer(getBuildingnumber,many=True)
        return render(request,"deleteflat.html",{"data":flats_serializer.data})
    except:
        return HttpResponse("Invalid Building Number")



@csrf_exempt
def delete_data_read(request):

    getId = request.POST.get("newid")
    ApiLink="http://127.0.0.1:8000/flats/viewaflat/" + getId
    requests.delete(ApiLink)
    return HttpResponse("Data deleted successfully")






