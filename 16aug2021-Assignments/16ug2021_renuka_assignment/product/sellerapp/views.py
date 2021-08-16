from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from sellerapp.serializers import SellerSerializer
import json
from sellerapp.models import Seller




@csrf_exempt
def seller_list(request):
    if (request.method=="GET"):
        sellers=Seller.objects.all()
        seller_serializer=SellerSerializer(sellers,many=True)
        return JsonResponse(seller_serializer.data,safe=False)



@csrf_exempt
def selleraddpage(request):
    if(request.method =="POST"):
        getId=request.POST.get("sellerid")
        getSellername=request.POST.get("sellername")
        getAddress=request.POST.get("address")
        getPhonenumber=request.POST.get("phonenumber")
        mydict={"sellerid":getId,"sellername":getSellername,"address":getAddress,"phonenumber":getPhonenumber}
        result=json.dumps(mydict)
        #return HttpResponse(result)
        seller_serialize=SellerSerializer(data=mydict)
        if (seller_serialize.is_valid()):
            seller_serialize.save()
            #return HttpResponse("success")
            return JsonResponse(seller_serialize.data)
        else:
            return HttpResponse("error in serialisation")
            
        # return HttpResponse(result)
    else:
        return HttpResponse("No get method is allowed")