from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
from rest_framework.parsers import JSONParser
from flats.serializers import FlatSerializer
from flats.models import Flat
from rest_framework import status
import requests
# Create your views here.

def homepage(request):
    return render(request,"home.html")

def addata(request):
    return render(request,"index.html")

def viewall(request):
    fetchdata=requests.get("http://127.0.0.1:8000/flats/viewall/").json()
    return render(request,"viewflat.html",{"data":fetchdata})

def searchbuildno(request):
    return render(request,"searchflat.html")

def updation(request):
    return render(request,"updateflat.html")

def deletion(request):
    return render(request,"deleteflat.html")


@csrf_exempt
def searchapi(request):
    try:
        getno=request.POST.get("buildingno")
        getflat=Flat.objects.filter(buildingno=getno)
        flat_serializer=FlatSerializer(getflat,many=True)
        return render(request,"searchflat.html",{"data":flat_serializer.data})
        return JsonResponse(flat_serializer.data,safe=False,status=status.HTTP_200_OK)
    
    except Flat.DoesNotExist:
        return HttpResponse("invalid",status=status.HTTP_404_NOT_FOUND)
    
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def updatesearchapi(request):
    try:
        getno=request.POST.get("buildingno")
        getflat=Flat.objects.filter(buildingno=getno)
        flat_serializer=FlatSerializer(getflat,many=True)
        return render(request,"updateflat.html",{"data":flat_serializer.data})
        return JsonResponse(flat_serializer.data,safe=False,status=status.HTTP_200_OK)
   
    except Flat.DoesNotExist:
        return HttpResponse("invalid",status=status.HTTP_404_NOT_FOUND)
    
    except:
        return HttpResponse("something went wrong")






@csrf_exempt
def updatedataread(request):
    getnewid=request.POST.get("newid")
    getnewbuildno=request.POST.get("newbuildno")
    getnewname=request.POST.get("newname")
    getnewaddress=request.POST.get("newaddress")
    getnewmob=request.POST.get("newmobnum")
    getnewadhaar=request.POST.get("newadhaar")
    getnewemail=request.POST.get("newemail")
    getnewpassword=request.POST.get("newpassword")

    mydata={'id':getnewid,'buildingno':getnewbuildno,'ownername':getnewname,'address':getnewaddress,'Mobnum':getnewmob,'adhaarno':getnewadhaar,'emailid':getnewemail,'password':getnewpassword}
    jsondata=json.dumps(mydata)
    apilink="http://127.0.0.1:8000/flats/viewone/" + getnewid
    requests.put(apilink,data=jsondata)
    return HttpResponse("data updated successfully")


@csrf_exempt
def deletesearchapi(request):
    try:
        getno=request.POST.get("buildingno")
        getflat=Flat.objects.filter(buildingno=getno)
        flat_serializer=FlatSerializer(getflat,many=True)
        return render(request,"deleteflat.html",{"data":flat_serializer.data})
        return JsonResponse(flat_serializer.data,safe=False,status=status.HTTP_200_OK)
   
    except Flat.DoesNotExist:
        return HttpResponse("invalid",status=status.HTTP_404_NOT_FOUND)
    
    except:
        return HttpResponse("something went wrong")


@csrf_exempt
def deletedataread(request):
    getnewid=request.POST.get("newid")

    apilink="http://127.0.0.1:8000/flats/viewone/" + getnewid
    requests.delete(apilink)
    return HttpResponse("data deleted successfully")







@csrf_exempt
def addflat(request):
    if(request.method=="POST"):
        #mydict=JSONParser().parse(request)
        flat_serialize=FlatSerializer(data=request.POST)
        if (flat_serialize.is_valid()):
            flat_serialize.save()
            return redirect(viewall)
            #return JsonResponse(flat_serialize.data,status=status.HTTP_200_OK)

        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    
    else:
        return HttpResponse("no get method allowed",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def viewall_list(request):
    if(request.method=="GET"):
        flatdata=Flat.objects.all()
        flat_serializer=FlatSerializer(flatdata,many=True)
        return JsonResponse(flat_serializer.data,safe=False)
        

        
@csrf_exempt
def flat_details(request, id):
    try:
        flatdata=Flat.objects.get(id=id)
    except Flat.DoesNotExist:
        return HttpResponse("Invalid id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        flat_serializer=FlatSerializer(flatdata)
        return JsonResponse(flat_serializer.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        flatdata.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)    
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        flat_serialize=FlatSerializer(flatdata,data=mydict)
        if (flat_serialize.is_valid()):
            flat_serialize.save()
            return JsonResponse(flat_serialize.data,status=status.HTTP_200_OK)
        

