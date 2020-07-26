from django.shortcuts import render
from django.shortcuts import render,redirect
from .form import RegisterForm
# Create your views here.
from django.http import HttpResponse
from .models import Product,Contact , Orders
from math import ceil
import json
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
def index(request):
     #products = Product.objects.all()
     #print(products)
    # n = len(products)
     #nSlides = n//4 + ceil((n/4)-(n//4))
    allProds=[]
    catprods=Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
     #params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
     #allProds = [[products, range(1, nSlides), nSlides],
               # [products, range(1, nSlides), nSlides]]
    params={'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about_us(request):
    return render(request, 'shop/about.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')
def productView(request,myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)

    return render(request, 'shop/prodView.html', {'product': product[0]})
def checkout(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '') +""+ request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(name=name, email=email, phone=phone, address=address, city=city, zip_code=zip_code)
        order.save()
        thank = True
        id = order.Order_Id
        return render(request, 'shop/checkout.html',{'thank':thank,'id':id})
    return render(request, 'shop/checkout.html')
def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')
def search(request):
    return render(request, 'shop/search.html')
def register(response):
    if response.method =="POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/shop")
    else:
        form = RegisterForm()


    return render(response,'shop/register.html', {"form": form})
