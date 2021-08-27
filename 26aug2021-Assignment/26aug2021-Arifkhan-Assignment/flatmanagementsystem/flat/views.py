from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from flat.models import Flat
from flat.serializers import FlatSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests

def registerflat(request):
    return render(request,'register.html')

def flatviewss(request):
    fetchdata=requests.get("http://127.0.0.1:8000/flat/viewall/").json
    return render(request,'view.html',{"data":fetchdata})

def flatsearch(request):
    return render(request,'search.html')

def flatupdate(request):
    return render(request,'update.html')

@csrf_exempt
def searchapi(request):
    try:
        getbuildingno=request.POST.get("bno")
        getbno=Flat.objects.filter(bno=getbuildingno)
        flat_serializer=FlatSerializer(getbno,many=True)
        
        return render(request,"search.html",{"data":flat_serializer.data})
    except Flat.DoesNotExist:
        return HttpResponse("Invalid building no")
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def addflat(request):
    if (request.method=="POST"):
        getbuildingno=int(request.POST.get('bno'))
        getname=request.POST.get('ownername')
        getaddress=request.POST.get('address')
        getmobilenumber=int(request.POST.get('mobileno'))
        getaddhar=request.POST.get('addharno')
        getemail=request.POST.get('email')
        getusername=request.POST.get('username')
        getpassword=request.POST.get('password')
        mydata={'bno':getbuildingno,'ownername':getname,'address':getaddress,'mobileno':getmobilenumber,'addharno':getaddhar,'email':getemail,'username':getusername,'password':getpassword}

        #mydata=JSONParser().parse(request)
        flat_serialize=FlatSerializer(data=mydata)
        
        if (flat_serialize.is_valid()):
            flat_serialize.save()
            return redirect(flatviewss)
            #return JsonResponse(flat_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def flat_all(request):
    if(request.method=="GET"):
        k=Flat.objects.all()
        flat_serializer=FlatSerializer(k,many=True)
        return JsonResponse(flat_serializer.data,safe=False)

@csrf_exempt
def flat_single(request,fetchid):
    
    sh=Flat.objects.get(id=fetchid)

    
    if(request.method=="GET"):
        flat_serialize=FlatSerializer(sh)
        return JsonResponse(flat_serialize.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        sh.delete()
        return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)
    if(request.method=="PUT"):
        mydata=JSONParser().parse(request)
        flat_serialize=FlatSerializer(sh,data=mydata)

        if(flat_serialize.is_valid()):
            flat_serialize.save()
            return JsonResponse(flat_serialize.data,status=status.HTTP_200_OK)
        else:
            return JsonResponse(flat_serialize.errors,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def updatesearchapi(request):
    try:
        getbuildingno=request.POST.get("bno")
        getflat=Flat.objects.filter(bno=getbuildingno)
        flat_serializer=FlatSerializer(getflat,many=True)

        return render(request,"update.html",{"data":flat_serializer.data})
    except Flat.DoesNotExist:
        return HttpResponse("Invalid bno code")
    except:
        return HttpResponse("something went wrong")
@csrf_exempt
def update_data_read(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        getbno=request.POST.get('newbno')
        getname=request.POST.get('newownername')
        getaddress=request.POST.get('newaddress')
        getmobilenumber=int(request.POST.get('newmobileno'))
        getaddhar=request.POST.get("newaddharno")
        getemail=request.POST.get("newemail")
        getusername=request.POST.get('newusername')
        getpassword=request.POST.get('newpassword')
        mydata={'bno':getbno,'ownername':getname,'address':getaddress,'mobileno':getmobilenumber,'addharno':getaddhar,'email':getemail,'username':getusername,'password':getpassword}
        jsondata=json.dumps(mydata)
        ApiLink="http://localhost:8000/flat/view/" +getnewid
        requests.put(ApiLink,data=jsondata)
        return HttpResponse("data has be updates successfully")

def flatdelete(request):
    return render(request,'delete.html')

@csrf_exempt
def deletesearchapi(request):
    try:
        getbuildingno=request.POST.get("bno")
        getflat=Flat.objects.filter(bno=getbuildingno)
        flat_serializer=FlatSerializer(getflat,many=True)
        return render(request,"delete.html",{"data":flat_serializer.data})
    except Flat.DoesNotExist:
        return HttpResponse("Invalid building no")
    except:
        return HttpResponse("something went wrong")
@csrf_exempt
def delete_data_read(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        ApiLink="http://localhost:8000/flat/view/" +getnewid
        requests.delete(ApiLink)
        return HttpResponse("data has be deleted successfully")