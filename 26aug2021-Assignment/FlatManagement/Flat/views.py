from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Flat.models import FlatModel
from Flat.serializer import FlatSerializer

# Create your views here.
@csrf_exempt
def home(request):
    return render(request,'home.html')


@csrf_exempt
def Add(request):
    if request.method=="POST":
        print("add")
        data1=FlatSerializer(data=request.POST)

        if data1.is_valid():
            data1.save()
            return JsonResponse(data1.data)
        else:
            HttpResponse(data1.errors)
    return render(request,'add.html')

@csrf_exempt
def viewall(request):
    details=FlatModel.objects.all()
    #data1=FlatSerializer(details,many=True)
    return render(request,'viewall.html',{'data':details})

@csrf_exempt
def search(request):
    if request.method=="POST":
        b=request.POST.get('bno')
        data1=FlatModel.objects.filter(bno=b)
        Flatdata=FlatSerializer(data1,many=True)
        return render(request,'search.html',{'data':data1})
    return render(request,'search.html')

@csrf_exempt
def update(request):
    if request.method=="GET":
        print("get")
        b=request.GET.get('bno')
        print(b)
        data1=FlatModel.objects.filter(bno=b)
        Flatdata=FlatSerializer(data1,many=True)
        print(data1)
        return render(request,'update.html',{'data':data1})
    if request.method=="POST":
        b=request.POST.get('bno')
        data1=FlatModel.objects.get(bno=b)
        details=FlatSerializer(request.POST)
        print(details.data)
        Flatdata=FlatSerializer(data1,data=details.data)
        print("Flat",Flatdata)
        if Flatdata.is_valid():
            Flatdata.save()
            return redirect (viewall)
        else:
            return HttpResponse(Flatdata.errors)
    return render(request,'update.html')

@csrf_exempt
def delete(request):
    if request.method=="POST":
        b=request.POST.get('bno')
        data1=FlatModel.objects.get(bno=b)
        data1.delete()
        return redirect(viewall)
    return render(request,'delete.html')





