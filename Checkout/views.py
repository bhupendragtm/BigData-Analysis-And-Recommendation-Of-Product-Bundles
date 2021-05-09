from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ProductBundleRecommendation.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from .models import Order,Product
from django.template.loader import render_to_string
# Create your views here.
@login_required(login_url='/account/login/')
def checkout(request):
    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST["email"]
        address = request.POST["address"]
        city = request.POST["city"]
        province = request.POST["province"]
        zipcode = request.POST["zip"]
        product_name = request.POST["product_name"]
        
        total = request.POST["total"]
        print(email,product_name,total)
        obj = Order(name=name,email=email,address=address,city=city,province=province,zipcode=zipcode)
        obj.save()

        product_obj = Product()
        product_obj.order = obj
        product_obj.product_D = product_name
        product_obj.total = total
        product_obj.save()
        product_name = product_name.split("qty:")
        product_name = ''.join(product_name)
        product_name = product_name.split()
        print(product_name)
        
        product_name_only =[]
        product_name_qty = []
        
        for i,char in enumerate(product_name):
            if(i%2==0):
                product_name_only.append(char)
            else:
                product_name_qty.append(char)
        
        product_name_details = zip(product_name_only,product_name_qty) 
        context = {'order_id':obj.id,'username':name,'date':obj.date,'address':address,'city':city,'province':province,'total':total,'product_name_details':product_name_details}
        html_message = render_to_string('Checkout/mail_message.html',context)
        send_mail("Your Instacart order has received!", "Thank you for your order", EMAIL_HOST_USER, [email],html_message=html_message,fail_silently=False)
        return render(request,'Checkout/order_success.html',{'recepient':email,'order_id':obj.id })
    else:
        
        return render(request,'Checkout/checkout.html')