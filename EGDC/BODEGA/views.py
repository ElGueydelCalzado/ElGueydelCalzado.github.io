from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


class NewSkuForm(forms.Form):
    sku = forms.CharField(label="Nuevo SKU")

# Create your views here.
def index(request):
    if "BODEGA" not in request.session:
        request.session["skus"] = []

    return render(request, "bodega/index.html", {
        "sku": request.session["skus"]
    })

def searchSKU(request, sku):
    return render(request, "bodega/index.html", {
        "sku": sku
    })

def addSKU(request):
    if request.method == "POST":
        form = NewSkuForm(request.POST)
        if form.is_valid():
            sku = form.cleaned_data["sku"]
            request.session["skus"] += [sku]
            return HttpResponseRedirect(reverse("bodega:index"))
        else:
            return render(request, "bodega/addSKU.html", {
                "form": form
            })
    return render(request, "bodega/addSKU.html", {
        "form": NewSkuForm()
    })