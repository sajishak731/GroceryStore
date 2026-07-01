
from django.shortcuts import render,redirect
from django.template.context_processors import request

from AdminApp.models import CategoryDb,ProductDb
from WebApp.models import ContactDb,RegistrationDb,CartDb
from django.contrib import messages

# Create your views here.


def homepage(request):
    categories= CategoryDb.objects.all()
    sing_cat = CategoryDb.objects.all()[:4]
    products = ProductDb.objects.all()[:8]
    sing_products = ProductDb.objects.filter(category_name='vegetables')
    cart_total=0
    uname=request.session['name']
    if uname:
        cart_total = CartDb.objects.filter(UserName=uname).count()

    context ={'categories':categories,'products':products,'sing_cat':sing_cat,
                                       'sing_products':sing_products,'cart_total':cart_total}
    return render(request,'home.html',context)

def product_page(request):
    products = ProductDb.objects.all()
    categories = CategoryDb.objects.all()[:5]
    categories_1 = CategoryDb.objects.all()

    featured_product = ProductDb.objects.all()[:5]
    cart_total = 0
    uname = request.session['name']
    if uname:
        cart_total = CartDb.objects.filter(UserName=uname).count()

    context ={
        'products': products, 'categories': categories, 'featured': featured_product,'cart_total':cart_total,'categories_1':categories_1,
    }
    return render(request,'produtcs.html',context)

def about_page(request):
    categories= CategoryDb.objects.all()
    cart_total = 0
    uname = request.session['name']
    if uname:
        cart_total = CartDb.objects.filter(UserName=uname).count()

    context ={'categories':categories,'cart_total':cart_total}
    return render(request,'about_us.html',context)

def contact_page(request):
    categories= CategoryDb.objects.all()
    cart_total = 0
    uname = request.session['name']
    if uname:
        cart_total = CartDb.objects.filter(UserName=uname).count()

    context ={'categories':categories,'cart_total':cart_total}

    return render(request,'contact.html',context)

def filtered_product(request,cat_name):
    products = ProductDb.objects.filter(category_name=cat_name)
    categories = CategoryDb.objects.all()[:5]
    categories_1 = CategoryDb.objects.all()

    featured_product = ProductDb.objects.all()[:5]
    cart_total = 0
    uname = request.session['name']
    if uname:
        cart_total = CartDb.objects.filter(UserName=uname).count()
    context = {
        'categories':categories,
        'products':products,
        'featured_product':featured_product,
        'cart_total':cart_total,
        'categories_1':categories_1,

    }
    return render(request,'filtered_products.html',context)


def single_item(request,pro_id):
    products = ProductDb.objects.get(id=pro_id)
    categories = CategoryDb.objects.all()[:5]
    featured_product = ProductDb.objects.all()[:5]
    cart_total = 0
    uname = request.session['name']
    if uname:
        cart_total = CartDb.objects.filter(UserName=uname).count()
    context ={
        'products': products, 'categories': categories,
        'featured_product':featured_product,
        'cart_total':cart_total,
    }


    return render(request,'single_item.html',context)


def contactpage(req):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        obj = ContactDb(name=name,email=email,subject=subject,message=message)
        obj.save()
        return redirect(contactpage)

def contact_save(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        obj = ContactDb(name=name,email=email,subject=subject,message=message)
        obj.save()
        return redirect(contact_page)

def user_registration(req):
    return render(req,'registration.html')

def user_sign_up(request):
    if request.method == "POST":
        name =request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pswd')
        con_password = request.POST.get('cpswd')
        obj =RegistrationDb(name=name,email=email,password=password,confirm_password=con_password)
        if RegistrationDb.objects.filter(name=name).exists():
            print("username already existing....!")
            return redirect(homepage)

        elif RegistrationDb.objects.filter(email=email).exists():
            print("email already existing..!")
            return redirect(user_registration)
        else:
            obj.save()
            return redirect(homepage)
def user_sign_in(request):
    if request.method == "POST":
        name = request.POST.get('uname')
        pswd = request.POST.get('pswd')
        if RegistrationDb.objects.filter(name=name,password=pswd).exists():
             request.session['name']=name
             request.session['password'] =pswd
             return redirect(homepage)
        else:
            print("username already exists")
            return redirect(user_sign_in)
    else:
        print("invalid username")
        return redirect(user_registration)

def user_logout(request):
    del request.session["name"]
    del request.session["password"]
    messages.warning(request, "Logout succesfully....!")
    return redirect(user_registration)

def privacy_policy(req):
    return render(req,'privacy_policy.html')

def cartpage(req):
    return render(req,'cartpages.html')

def save_cart(request):
    if request.method == "POST":
        name =request.POST.get('uname')
        product_name=request.POST.get('product_name')
        quantity=request.POST.get('quantity')
        price=request.POST.get('price')
        totalprice=request.POST.get('total')
        product=ProductDb.objects.filter(product_name=product_name).first()
        img=product.product_image if product else None
        obj =CartDb(Product_Name=product_name,Quantity=quantity,Price=price,Total_Price=totalprice,UserName=name,Product_Img=img)
        obj.save()
        return redirect(cartpage_products)

def cartpage_products(request):
    data = CartDb.objects.filter(UserName=request.session['name'])
    cart_total = 0
    uname = request.session['name']
    if uname:
        cart_total = CartDb.objects.filter(UserName=uname).count()

    sub_total=0
    total_amount=0
    delivery_charge=0

    for i in data:
        sub_total += i.Total_Price
        if sub_total>1000:
            delivery_charge=50
        elif sub_total <=1000 and sub_total>=500:
            delivery_charge=70
        else:
            delivery_charge=100
        total_amount=sub_total+delivery_charge

    context={
            'data': data,
        'sub_total':sub_total,
        'delivery_charge':delivery_charge,
        'total_amount':total_amount,
        'cart_total':cart_total,

             }
    return render(request,'cartpages.html',context)

def delete_product(request,c_id):
    data = CartDb.objects.filter(id=c_id)
    data.delete()
    return redirect(cartpage_products)



def checkoutpage(request):
    categories= CategoryDb.objects.all()
    data = CartDb.objects.filter(UserName=request.session['name'])

    cart_total = 0
    uname = request.session['name']
    if uname:
        cart_total = CartDb.objects.filter(UserName=uname).count()
    sub_total = 0
    total_amount = 0
    delivery_charge = 0

    for i in data:
        sub_total += i.Total_Price
        if sub_total > 1000:
            delivery_charge = 50
        elif sub_total <= 1000 and sub_total >= 500:
            delivery_charge = 70
        else:
            delivery_charge = 100
        total_amount = sub_total + delivery_charge



    context ={'categories':categories,
              'cart_total':cart_total,'sub_total':sub_total,
              'data':data,'total_amount':total_amount,'delivery_charge':delivery_charge}


    return render(request,'checkout.html',context)



