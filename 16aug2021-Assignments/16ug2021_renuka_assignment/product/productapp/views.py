from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from productapp.serializers import ProductSerializer
import json
from productapp.models import Product




@csrf_exempt
def product_list(request):
    if (request.method=="GET"):
        products=Product.objects.all()
        product_serializer=ProductSerializer(products,many=True)
        return JsonResponse(product_serializer.data,safe=False)



@csrf_exempt
def productaddpage(request):
    if(request.method =="POST"):
        getCode=request.POST.get("pcode")
        getProductName=request.POST.get("pname")
        getProductDescription=request.POST.get("pdes")
        getProductPrice=request.POST.get("price")
        mydict={"pcode":getCode,"pname":getProductName,"pdes":getProductDescription,"price":getProductPrice}
        result=json.dumps(mydict)
        #return HttpResponse(result)
        product_serialize=ProductSerializer(data=mydict)
        if (product_serialize.is_valid()):
            product_serialize.save()
            #return HttpResponse("success")
            return JsonResponse(product_serialize.data)
        else:
            return HttpResponse("error in serialisation")
            
        # return HttpResponse(result)
    else:
        return HttpResponse("No get method is allowed")
