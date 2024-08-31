from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,staff,buyer,Seller
from rest_framework import generics
from .serializers import StaffSerializer
from .form import ProductForm,staffForm,sellerForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login
from django.contrib import messages

CATEGORY_CHOICES = [
    ('food', 'Food'),
    ('fruits', 'Fruits'),
    ('electronics', 'Electronics'),
    ('fabric', 'Fabric'),
    ('homedecore', 'Home Decor'),
    ('wooditem', 'Wood Item'),
]

def home(request):
    return render(request,'home.html',{})

def product(request):
    items=Product.objects.all()
    context={
        'items':items
    }
    return render(request,'product.html',context)

def product_delete(request, pk):
    item = get_object_or_404(Product, id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('product')
    return redirect('product')

def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product')  # Redirect to the list of products or any other page
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_update.html', {'form': form,'categories': CATEGORY_CHOICES})
    



def staf(request):
    items=staff.objects.all()
    context={
        'items':items
    }
    return render(request,'staff.html',context)
def update_staff(request, pk):
    Staff = get_object_or_404(staff, pk=pk)
    if request.method == "POST":
        form = staffForm(request.POST, instance=Staff)
        if form.is_valid():
            form.save()
            return redirect('staf')  
    else:
        form = staffForm(instance=product)
    return render(request, 'staff_update.html', {'form': form})
    


def login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return redirect('sin')
    return render(request,'login.html',{})


def signup(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user) 
            return redirect('product')
        else:
            messages.error(request,"username/password not exists")
            return redirect('login')
    return render(request,'signup.html',{})


def staffadd(request):
    if request.method == 'POST':
        staff_name= request.POST.get('staff_name')
        staff_email = request.POST.get('staff_email')
        staff_number = request.POST.get('staff_number')
        pro=staff.objects.create(staff_name=staff_name,staff_email=staff_email, staff_number=staff_number)
        pro.save()
        # print(pro)
        return redirect('staf')
    return render(request,'staffadd.html',{})

def staffadd_delete(request,pk):
    item = get_object_or_404(staff, id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('staf')
    return redirect('staf')






def productadd(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        quantity = request.POST.get('quantity')
        pro=Product.objects.create(name=name, category=category, quantity=quantity)
        pro.save()
        # print(pro)
        return redirect('product')
    
    return render(request,'productadd.html',{'categories': CATEGORY_CHOICES})



def seller(request):
    items=Seller.objects.all()
    context={
        'items':items
    }
    return render(request,'seller.html',context)

def selleradd(request):
    buyers = buyer.objects.all()
    if request.method == 'POST':
        seller_name = request.POST.get('seller_name')
        seller_email = request.POST.get('seller_email')
        seller_address = request.POST.get('seller_address')
        seller_number = request.POST.get('seller_number')
        seller_quantity = request.POST.get('seller_quantity')
        buyer_id = request.POST.get('buyer_id')

        if not buyer_id or not buyer_id.isdigit():
            return render(request, 'selleradd.html', {
                'error': 'A valid buyer must be selected',
                'buyers': buyers
            })
        try:
            # Fetch the Buyer instance
            Buyer = buyer.objects.get(id=int(buyer_id))
        except Buyer.DoesNotExist:
            return render(request, 'selleradd.html', {
                'error': 'Invalid buyer selected',
                'buyers': buyers
            })
        seller = Seller.objects.create(
            seller_name=seller_name,
            seller_email=seller_email,
            seller_address=seller_address,
            seller_number=seller_number,
            seller_quantity=seller_quantity,
            Buyer=Buyer
        )
        seller.save()

        return redirect('seller')
    return render(request,'selleradd.html',{'buyers': buyers})

def seller_delete(request,pk):
    item = get_object_or_404(Seller, id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('seller')
    return redirect('seller')

def update_seller(request, pk):
    seller = get_object_or_404(Seller, pk=pk)
    buyers = buyer.objects.all()
    if request.method == "POST":
        form = sellerForm(request.POST, instance=seller)
        if form.is_valid():
            form.save()
            return redirect('seller')  # Redirect to the list of products or any other page
    else:
        form = staffForm(instance=seller)
    return render(request, 'seller_update.html', {'form': form,'buyers': buyers})

