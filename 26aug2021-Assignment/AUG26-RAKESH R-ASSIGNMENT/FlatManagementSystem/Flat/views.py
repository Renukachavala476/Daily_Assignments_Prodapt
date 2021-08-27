from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from Flat.serializers import FlatSerializer
from Flat.models import Flat
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests


@csrf_exempt
def update_data_read(request):
    getId=request.POST.get("newid")

    getFlatno=request.POST.get("newflatno")    
    getBuildingno=request.POST.get("newbuildingno")
    getOwnername=request.POST.get("newownername")
    getMobileno=request.POST.get("newmobileno")
    getAddress=request.POST.get("newaddress")
    getAadharno=request.POST.get("newaadharno")
    getEmailid=request.POST.get("newemailid")
    getPassword=request.POST.get("newpassword")
    
    mydata={'flat_no':getFlatno,'building_no':getBuildingno,'owner_name':getOwnername,'mobile_no':getMobileno,'address':getAddress,'aadhar_no':getAadharno,'email_id':getEmailid,'password':getPassword}
    jsondata=json.dumps(mydata)
    ApiLink="http://127.0.0.1:8000/Flat/viewflat/" + getId
    requests.put(ApiLink,data=jsondata)
    return HttpResponse("Data updated successfully")
@csrf_exempt
def delete_data_read(request):
   
    getId=request.POST.get("newid")

   
    ApiLink="http://127.0.0.1:8000/Flat/viewflat/" + getId
    requests.delete(ApiLink)
    return HttpResponse("Data deleted successfully")    
@csrf_exempt
def searchapi(request):
    try:
        getBuildingno=request.POST.get("building_no")
        getBuildnos=Flat.objects.filter(building_no=getBuildingno)
        flat_serialize=FlatSerializer(getBuildnos,many=True)
        return render(request,"search.html",{"data":flat_serialize.data})
    except:   
        return HttpResponse("Invalid Building no",status=status.HTTP_404_NOT_FOUND)
@csrf_exempt
def update_search_api(request):
    try:
        getFlatno=request.POST.get("flat_no")
        getFlatnos=Flat.objects.filter(flat_no=getFlatno)
        flat_serialize=FlatSerializer(getFlatnos,many=True)
       
        return render(request,"update.html",{"data":flat_serialize.data})
    except:   
        return HttpResponse("Invalid Flat no",status=status.HTTP_404_NOT_FOUND)
@csrf_exempt
def delete_search_api(request):
    try:
        getFlatno=request.POST.get("flat_no")
        getFlatnos=Flat.objects.filter(flat_no=getFlatno)
        flat_serialize=FlatSerializer(getFlatnos,many=True)
        return render(request,"delete.html",{"data":flat_serialize.data})
    except:   
        return HttpResponse("Invalid Flat no")
def register(request):
    return render(request,'register.html')
def viewall(request): 
    fetchdata=requests.get("http://127.0.0.1:8000/Flat/viewall/").json()
    return render(request,'view.html',{"data":fetchdata})
def update(request):
    return render(request,'update.html') 
def delete(request):
    return render(request,'delete.html')  
def search_flat(request):
    return render(request,'search.html') 
def home(request):
    return render(request,'home.html')
def contact(request):
    return render(request,'contact.html')                        
@csrf_exempt
def flat_details(request,fetchid):
    try:
        flat=Flat.objects.get(id=fetchid)
        if(request.method=="GET"):
            flat_serializer=FlatSerializer(flat)
            return JsonResponse(flat_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            flat.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            flat_serialize=FlatSerializer(flat,data=mydata)
            if(flat_serialize.is_valid()):
                flat_serialize.save()
                return JsonResponse(flat_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(flat_serialize.errors,status=status.HTTP_400_BAD_REQUEST)    
    except Notes.DoesNotExist:
        return HttpResponse("Invalid Flat no",status=status.HTTP_404_NOT_FOUND)
    
        


@csrf_exempt
def flat_list(request):
    if(request.method=="GET"):
        flat=Flat.objects.all()
        flat_serializer=FlatSerializer(flat,many=True)
        return JsonResponse(flat_serializer.data,safe=False)


@csrf_exempt
def flatsPage(request):
    if(request.method=="POST"):
        flat_serialize=FlatSerializer(data=request.POST)
        if(flat_serialize.is_valid()):
            flat_serialize.save()
            return redirect(viewall)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)    
      
    else:
        return HttpResponse("No GET method Allowed",status=status.HTTP_404_NOT_FOUND)
        
