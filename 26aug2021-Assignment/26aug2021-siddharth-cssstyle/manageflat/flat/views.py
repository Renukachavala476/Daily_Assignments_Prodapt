from django import http
from django.shortcuts import render
from django.http import HttpResponse,response
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
from flat.models import Flats
from flat.serializers import FlatSerializer

@csrf_exempt
def addFlats(request):
    if(request.method=="POST"):
        # mydata=JSONParser().parse(request)
        flatserialize=FlatSerializer(data=request.POST)
        if (flatserialize.is_valid()):
            flatserialize.save() 
            return response.JsonResponse(flatserialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error")
    else:
        return HttpResponse("error in serialization process of flats")

def register(request):
    return render(request,'register.html')



@csrf_exempt
def viewFlats(request):
    if (request.method=='GET'):
        f1=Flats.objects.all()
        flatserial=FlatSerializer(f1,many=True)
        return response.JsonResponse(flatserial.data, safe=False)

def flatview(request):
    fetch=requests.get("http://127.0.0.1:8000/flat/viewflat/").json()
    return render(request,'viewflat.html',{"data":fetch})




@csrf_exempt
def viewFlatdetails(request,id):
    try:
        f1=Flats.objects.get(id=id)
        if (request.method=='GET'):
            flatserial=FlatSerializer(f1) 
            return response.JsonResponse(flatserial.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=='DELETE'):
            f1.delete()
            return HttpResponse("Flat is removed")
        if (request.method=='PUT'):
            mydata=JSONParser().parse(request)
            flatserial=FlatSerializer(f1,data=mydata)
            if (flatserial.is_valid()):
                flatserial.save()
                return response.JsonResponse(flatserial.data,status=status.HTTP_200_OK)
    except Flats.DoesNotExist:
        return HttpResponse("invalid ID ")




@csrf_exempt
def searchapi(request):
    try:
        getbuildnum=request.POST.get("buildnum")
        getflat=Flats.objects.filter(buildnum=getbuildnum)
        flatserial=FlatSerializer(getflat,many=True)
        # return response.JsonResponse(flatserial.data,safe=False)
        return render(request,"search.html",{"data":flatserial.data})
    except Flats.DoesNotExist:
        return HttpResponse("invalid building number")
    except:
        return HttpResponse("something went wrong")

def searchflat(request):
    return render(request,'search.html')





@csrf_exempt
def updatesearchapi(request):
    try:
        getbuildnum=request.POST.get("buildnum")
        getFlat=Flats.objects.filter( buildnum=getbuildnum)
        Flat_serializer=FlatSerializer(getFlat,many=True)
        # return JsonResponse(Flat_serializer.data,safe=False,status=status.HTTP_200_OK)
        return render(request,"update.html",{"data":Flat_serializer.data})
    except Flats.DoesNotExist:
        return HttpResponse("Invalid building number")
    except:
        return HttpResponse("something went wrong")
@csrf_exempt
def update_data_read(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        getbuildnum=request.POST.get('newbuildnum')
        getname=request.POST.get('newname')
        getAddress=request.POST.get('newaddress')
        getMobile=request.POST.get('newmobile')
        getaadhar=int(request.POST.get('newaadhar'))
        getemail=request.POST.get('newemail')
    
        mydata={'buildnum':getbuildnum,'name':getname,'address':getAddress,'mobile':getMobile,'aadhar':getaadhar,'email':getemail}
        jsondata=json.dumps(mydata)
        ApiLink="http://localhost:8000/flat/viewflatdetails/" +getnewid
        requests.put(ApiLink,data=jsondata)
        return HttpResponse("data has be updates successfully")

def update(request):
    return render(request,'update.html')

    


@csrf_exempt
def deletesearchapi(request):
    try:
        getbuildnum=request.POST.get("buildnum")
        getFlat=Flats.objects.filter( buildnum=getbuildnum)
        Flat_serializer=FlatSerializer(getFlat,many=True)
        # return JsonResponse(Flat_serializer.data,safe=False,status=status.HTTP_200_OK)
        return render(request,"delete.html",{"data":Flat_serializer.data})
    except Flats.DoesNotExist:
        return HttpResponse("Invalid building number")
    except:
        return HttpResponse("something went wrong")
@csrf_exempt
def delete_data_read(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        
        ApiLink="http://localhost:8000/flat/viewflatdetails/" +getnewid
        requests.delete(ApiLink)
        return HttpResponse("data has be deleted successfully")

def delete(request):
    return render(request,'delete.html')



