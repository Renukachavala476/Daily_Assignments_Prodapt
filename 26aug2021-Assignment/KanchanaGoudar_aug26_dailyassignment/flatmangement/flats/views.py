from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from flats.serialize import FlatSerialize
from flats.models import Flats
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
def Addflats(request):
    return render(request,'Add.html')
def Viewflats(request):
    fetchdata=requests.get("http://127.0.0.1:8000/flats/display/").json()
    return render(request,'views.html',{"data":fetchdata})
def searchflats(request):
    return render(request,'search.html')
def updateflats(request):
    return render(request,'update.html')
def deleteflats(request):
    return render(request,'delete.html')

@csrf_exempt
def Insert_Flats(request):
    if(request.method=="POST"):
        Flat_serialize=FlatSerialize(data=request.POST)
        if (Flat_serialize.is_valid()):
            Flat_serialize.save()
            return redirect(Viewflats)
        else:
            return HttpResponse("error in serialization")
    else:
        return HttpResponse("no get method is allowed")

@csrf_exempt
def Display(request):
    if (request.method=="GET"):

        flats=Flats.objects.all()
        flats_s=FlatSerialize(flats,many=True)
        return JsonResponse(flats_s.data,safe=False)
@csrf_exempt
def displayflats(request,fetchid):
    try:
        flats=Flats.objects.get(id=fetchid)
        if (request.method=="GET"):
            flat_serializer=FlatSerialize(flats)
            return JsonResponse(flat_serializer.data,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            flats.delete()
            return HttpResponse("delted")
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            Flat_serialize=FlatSerialize(flats,data=mydata)
            if (Flat_serialize.is_valid()):
                Flat_serialize.save()
                return JsonResponse(Flat_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(Flat_serialize.errors)

    except Flats.DoesNotExist:
        return HttpResponse("Invalid Flat Id",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def searchapi(request):
    try:
        getBuildingno=request.POST.get("Bno")
        getflats=Flats.objects.filter(Bno=getBuildingno)
        flat_s=FlatSerialize(getflats,many=True)
        return render(request,"search.html",{"data":flat_s.data})
    except Flats.DoesNotExist:
        return HttpResponse("Invalid Building number",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something went wrong")

@csrf_exempt
def update_searchapi(request):
    try:
        getBuildingno=request.POST.get("Bno")
        getflats=Flats.objects.filter(Bno=getBuildingno)
        flat_s=FlatSerialize(getflats,many=True)
        return render(request,"update.html",{"data":flat_s.data})
    except Flats.DoesNotExist:
        return HttpResponse("Invalid Building number",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something went wrong")
@csrf_exempt
def update_data_read(request):
    getId=request.POST.get("newid")
    # print(getId)
    getBuildingno=request.POST.get("newBno")
    getOwner=request.POST.get("newOname")
    getmobile=request.POST.get("newMobile")
    getadress=request.POST.get("newAdress")
    getadahar=request.POST.get("newAdahar")
    getemail=request.POST.get("newEmailid")
    getpassword=request.POST.get("newPassword")
    mydata={"Bno":getBuildingno,"Oname":getOwner,"Mobile":getmobile,"Adress":getadress,"Adahar":getadahar,"Emailid":getemail,"Password":getpassword}
    jsondata=json.dumps(mydata)
    print(jsondata)
    ApiLink="http://127.0.0.1:8000/flats/displaynew/"+getId
    requests.put(ApiLink,data=jsondata)
    return redirect(Viewflats)

@csrf_exempt
def delete_searchapi(request):
    try:
        getBuildingno=request.POST.get("Bno")
        getflats=Flats.objects.filter(Bno=getBuildingno)
        flat_s=FlatSerialize(getflats,many=True)
        return render(request,"delete.html",{"data":flat_s.data})
    except Flats.DoesNotExist:
        return HttpResponse("Invalid Building number",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something went wrong")

@csrf_exempt
def delete_data_read(request):
   
    getId=request.POST.get("newid")

   
    ApiLink="http://127.0.0.1:8000/flats/displaynew/"+ getId
    requests.delete(ApiLink)
    return redirect(Viewflats)
  

#     {
#     "id": 1,
#     "Bno": "5",
#     "Oname": "Sinchi",
#     "Mobile": "9591359139",
#     "Adress": "Sirsi",
#     "Adahar": "43567895321",
#     "Emailid": "kanchanagoudar123@gmail.com",
#     "Password": "Kanchana@8+"
# }
