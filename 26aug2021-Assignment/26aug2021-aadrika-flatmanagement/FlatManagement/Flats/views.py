from django import http
from django.shortcuts import render
from django.http import HttpResponse,response
import json
from django.views.decorators.csrf import csrf_exempt
from Flats.serializers import FlatsSerializer
from Flats.models import Flat
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests

@csrf_exempt
def addFlat(request):
    if(request.method=="POST"):
        # mydata=JSONParser().parse(request)
        flatserialize=FlatsSerializer(data=request.POST)
        if (flatserialize.is_valid()):
            flatserialize.save() 
            return response.JsonResponse(flatserialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error")
    else:
        return HttpResponse("error in serialization process of flats")

@csrf_exempt
def viewFlat(request):
    if (request.method=='GET'):
        flat=Flat.objects.all()
        flatserial=FlatsSerializer(flat,many=True)
        return response.JsonResponse(flatserial.data, safe=False)

@csrf_exempt
def viewFlatdetails(request,id):
    try:
        flat=Flat.objects.get(id=id)
        if (request.method=='GET'):
            flatserial=FlatsSerializer(flat) 
            return response.JsonResponse(flatserial.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=='DELETE'):
            flat.delete()
            return HttpResponse("deleted Flat")
        if (request.method=='PUT'):
            mydata=JSONParser().parse(request)
            flatserial=FlatsSerializer(flat,data=mydata)
            if (flatserial.is_valid()):
                flatserial.save()
                return response.JsonResponse(flatserial.data,status=status.HTTP_200_OK)
    except Flat.DoesNotExist:
        return HttpResponse("invalid ID ")

def searchflat(request):
    return render(request,'search.html')

@csrf_exempt
def searchapi(request):
    try:
        getbuildnum=request.POST.get("buildnum")
        getflat=Flat.objects.filter(buildnum=getbuildnum)
        flatserial=FlatsSerializer(getflat,many=True)
        # return response.JsonResponse(flatserial.data,safe=False)
        return render(request,"search.html",{"data":flatserial.data})
    except Flat.DoesNotExist:
        return HttpResponse("invalid flat name")
    except:
        return HttpResponse("not runned")



def register(request):
    return render(request,'register.html')

def flatview(request):
    fetch=requests.get("http://127.0.0.1:8000/flats/viewflat/").json()
    return render(request,'viewflat.html',{"data":fetch})
    
def update(request):
    return render(request,'update.html')
    
def delete(request):
    return render(request,'delete.html')







@csrf_exempt
def updatesearchapi(request):
    try:
        getbuildnum=request.POST.get("buildnum")
        getFlat=Flat.objects.filter( buildnum=getbuildnum)
        Flat_serializer=FlatsSerializer(getFlat,many=True)
        # return JsonResponse(Flat_serializer.data,safe=False,status=status.HTTP_200_OK)
        return render(request,"update.html",{"data":Flat_serializer.data})
    except Flat.DoesNotExist:
        return HttpResponse("Invalid Flat code")
    except:
        return HttpResponse("something went wrong")
@csrf_exempt
def update_data_read(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        getbuildnum=request.POST.get('newbuildnum')
        getoname=request.POST.get('newoname')
        getAddress=request.POST.get('newaddress')
        getMobile=request.POST.get('newmobile')
        getadhar=int(request.POST.get('newadhar'))
        getemail=request.POST.get('newemail')
    
        mydata={'buildnum':getbuildnum,'oname':getoname,'address':getAddress,'mobile':getMobile,'adhar':getadhar,'email':getemail}
        jsondata=json.dumps(mydata)
        ApiLink="http://localhost:8000/flats/viewflatdetails/" +getnewid
        requests.put(ApiLink,data=jsondata)
        return HttpResponse("data has be updates successfully")


@csrf_exempt
def deletesearchapi(request):
    try:
        getbuildnum=request.POST.get("buildnum")
        getFlat=Flat.objects.filter( buildnum=getbuildnum)
        Flat_serializer=FlatsSerializer(getFlat,many=True)
        # return JsonResponse(Flat_serializer.data,safe=False,status=status.HTTP_200_OK)
        return render(request,"delete.html",{"data":Flat_serializer.data})
    except Flat.DoesNotExist:
        return HttpResponse("Invalid Flat code")
    except:
        return HttpResponse("something went wrong")
@csrf_exempt
def delete_data_read(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        # getbuildnum=request.POST.get('newbuildnum')
        # getoname=request.POST.get('newoname')
        # getAddress=request.POST.get('newaddress')
        # getMobile=request.POST.get('newmobile')
        # getadhar=int(request.POST.get('newadhar'))
        # getemail=request.POST.get('newemail')
    
        # mydata={'buildnum':getbuildnum,'oname':getoname,'address':getAddress,'mobile':getMobile,'adhar':getadhar,'email':getemail}
        # jsondata=json.dumps(mydata)
        ApiLink="http://localhost:8000/flats/viewflatdetails/" +getnewid
        requests.delete(ApiLink)
        return HttpResponse("data has be deleted successfully")

