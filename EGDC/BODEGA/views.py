from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "bodega/index.html")

def searchSKU(request, sku):
    return render(request, "bodega/index.html", {
        "sku": sku
    })

def addSKU(request):
    return HttpResponse("Page to Request to ADD a new Item!!")