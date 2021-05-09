from django.shortcuts import render,redirect
import json
from . import recomendation

# Create your views here.

# index page
def index(request):
    #get the topproductsbundles 
    topproductbundles=recomendation.topproductbundledetails()
    availableproducts = recomendation.availableproducts()
    #lets combine the no. and record using zip() and pass through dict
    i= range(len(topproductbundles))
    topproductbundles=topproductbundles
    zippedBundles = zip(i,topproductbundles)
    context ={
        'zippedBundles':zippedBundles,
        'items':availableproducts
    }
    return render(request,'Recommendation/index.html',context)

#addtocart tab get approach
def productsearch(request):
     #get the topproductsbundles 
    topproductbundles=recomendation.topproductbundledetails()
    availableproducts = recomendation.availableproducts()
    #lets combine the no. and record using zip() and pass through dict
    i= range(len(topproductbundles))
    topproductbundles=topproductbundles
    zippedBundles = zip(i,topproductbundles)

    if request.GET.get("product_name"):
        if(request.GET.get("recom")):
            Num_of_recom = request.GET["recom"]
        else:
            Num_of_recom = "8"
        product_name = request.GET["product_name"]
        print(product_name);
        recommendproducts = recomendation.getRecommend(product_name, int(Num_of_recom))
    
        context ={
            'zippedBundles':zippedBundles,
            'recommendations':recommendproducts,
            'items':availableproducts
        }
        return render(request,'Recommendation/index.html',context)

    else:
        context ={
            'zippedBundles':zippedBundles,
            'error_get':"Please specify the product name",
            'items':availableproducts
        }
        return render(request,'Recommendation/index.html',context)
    
