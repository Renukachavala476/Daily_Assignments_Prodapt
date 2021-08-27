from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from flats.models import Flats
from flats.serializers import FlatsSerializers
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
import requests,json


def flat(request):
    return render(request,'index.html')
def viewFlat(request):
    fetch = requests.get("http://127.0.0.1:8000/flats/viewall/").json()

    return render(request,'views.html',{"data":fetch})
def updateFlat(request):
    return render(request,'update.html')
def deleteFlat(request):
    return render(request,'delete.html')
def searchFlat(request):
    return render(request,'search.html')



@csrf_exempt
def update_search(request):
    try:
        getBuildingno = request.POST.get("buildingno")
        getBno = Flats.objects.filter(buildingno = getBuildingno )
        flat_serializer = FlatsSerializers(getBno,many=True)
        return render(request,'update.html',{"data":flat_serializer.data})
        # return JsonResponse(flat_serializer.data,safe=False,status=status.HTTP_200_OK)
    except:
        return HttpResponse("No Flats found",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def update_data(request):
    getnewid = request.POST.get("newid")
    getbuildingno = request.POST.get("newbuildingno")
    getownername = request.POST.get("newownername")
    getaddress = request.POST.get("newaddress")
    getmobno = request.POST.get("newmobno")
    getaadharno = request.POST.get("newaadharno")
    getemail = request.POST.get("newemail")
    getpassword = request.POST.get("newpassword")
    mydata= {"buildingno":getbuildingno,"ownername":getownername,"address":getaddress,"mobno":getmobno,"aadharno":getaadharno,"email":getemail,"password":getpassword}
    jsondata = json.dumps(mydata)
    apilink = "http://127.0.0.1:8000/flats/view/"+getnewid
    requests.put(apilink,data = jsondata)
    return HttpResponse("Data Updated Successfully")

@csrf_exempt
def delete_search(request):
    try:
        getBuildingno = request.POST.get("buildingno")
        getBno = Flats.objects.filter(buildingno = getBuildingno )
        flat_serializer = FlatsSerializers(getBno,many=True)
        return render(request,'delete.html',{"data":flat_serializer.data})
        # return JsonResponse(flat_serializer.data,safe=False,status=status.HTTP_200_OK)
    except:
        return HttpResponse("No Flats found",status=status.HTTP_404_NOT_FOUND)
    

    


@csrf_exempt
def delete_data(request):
    getnewid = request.POST.get("newid")
    apilink = "http://127.0.0.1:8000/flats/view/"+getnewid
    requests.delete(apilink)
    return HttpResponse("Data deleted Successfully")





@csrf_exempt
def searchapi(request):
    try:
        getBuildingno = request.POST.get("buildingno")
        getFlat = Flats.objects.filter(buildingno = getBuildingno )
        flat_serializer = FlatsSerializers(getFlat,many=True)
        return render(request,'search.html',{"data":flat_serializer.data})
        # return JsonResponse(flat_serializer.data,safe=False,status=status.HTTP_200_OK)
    except:
        return HttpResponse("No Data found",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def addFlat(request):
    if(request.method == "POST"):
        # mydata = JSONParser().parse(request)
        flat_serializer = FlatsSerializers(data = request.POST)
        if(flat_serializer.is_valid()):
            flat_serializer.save()
            return JsonResponse(flat_serializer.data)
        else:
            return HttpResponse("Error in Serialization")

    else:
        return HttpResponse("GET method not allowed")

@csrf_exempt
def viewall(request):
    if(request.method == "GET"):
        flats = Flats.objects.all()
        flat_serializer = FlatsSerializers(flats, many=True)
        return JsonResponse(flat_serializer.data, safe=False)

@csrf_exempt
def view(request,id):
    try:
        flat = Flats.objects.get(id = id)
        if(request.method == "GET"):
            flat_serializer = FlatsSerializers(flat)
            return JsonResponse(flat_serializer.data, safe=False)

        if(request.method == "DELETE"):
            flat.delete()
            return HttpResponse("Deleted Successfully")

        if(request.method == "PUT"):
            mydict = JSONParser().parse(request)
            flat_serialize = FlatsSerializers(flat, data = mydict)
            if(flat_serialize.is_valid()):
                flat_serialize.save()
                return JsonResponse(flat_serialize.data, status=status.HTTP_200_OK)

    except Flats.DoesNotExist:
        return HttpResponse("Invalid Flat id",status=status.HTTP_404_NOT_FOUND)

