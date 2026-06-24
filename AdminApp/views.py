from django.shortcuts import render,redirect
from AdminApp.models import CategoryDb,ProductDb
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from WebApp.models import ContactDb

# Create your views here.

def loginpage(request):
    return render(request,'loginpage.html')


def dashboard(request):
    return render(request,'dashboard.html')

def add_category(request):
    return render(request,'add_categories.html')

def insert_category(request):
    if request.method == "POST":
        category_name = request.POST.get('name')
        description = request.POST.get('description')
        category_image = request.FILES.get('Image')
        obj = CategoryDb(category_image=category_image,description=description,category_name=category_name)
        obj.save()
        return redirect(add_category)

def admin_login(request):
    if request.method== "POST":
        uname = request.POST.get('username')
        pswd = request.POST.get('password')
        if User.objects.filter(username__contains = uname).exists():
            x = authenticate(username = uname,password = pswd)
            if x is not None:
                login(request,x)
                request.session["username"] =uname
                request.session["password"] =pswd
                print("Login succesfully...!")
                return redirect(dashboard)
            else:
                print("please enter correct username and password ")
                return redirect(dashboard)
        else:
            print("username not found")
            return redirect(dashboard)
def admin_logout(request):
    del request.session["username"]
    del request.session["password"]
    return redirect(loginpage)


def view_category(request):
    data = CategoryDb.objects.all()
    return render(request,'view_category.html',{'data':data})

def edit_category(request,t_id):
    data = CategoryDb.objects.get(id=t_id)
    return  render(request,'edit_category.html',{'data':data})

def update_category(request,c_id):
    category_name = request.POST.get('name')
    description = request.POST.get('description')
    try:
        img = request.FILES['Image']
        obj = FileSystemStorage()
        file =obj.save(img.name,img)
    except MultiValueDictKeyError:
        file = CategoryDb.objects.get(id=c_id).category_image
    CategoryDb.objects.filter(id=c_id).update(category_name=category_name,description=description,category_image=file)
    return redirect(view_category)

def delete_category(request,c_id):
    data = CategoryDb.objects.filter(id =c_id)
    data.delete()
    return redirect(view_category)
# ------------------------------------------------------------------------------------------------------------------------------------------
def new_product(request):
    data = CategoryDb.objects.all()
    return render(request,'products_add.html',{'data':data})


def view_product(request):
    data = ProductDb.objects.all()
    return render(request, 'view_products.html', {'data': data})

def edit_product(request,pro_id):
    pro = ProductDb.objects.get(id=pro_id)
    categories = CategoryDb.objects.all()
    return render(request,'products_edit.html',{'pro':pro,'categories':categories})

def display_product(request):
    data = ProductDb.objects.all()
    return render(request,'display_products.html',{'data': data})


def insert_product(request):
    if request.method == "POST":
        category_name = request.POST.get('category_name')
        product_name=request.POST.get('product_name')
        description = request.POST.get('description')
        product_image = request.FILES.get('product_image')
        price=request.POST.get('price')
        obj = ProductDb(product_image=product_image,product_name=product_name,description=description,category_name=category_name,price=price)
        obj.save()
        return redirect(new_product)
def update_product(request,p_id):
    category_name = request.POST.get('category_name')
    product_name = request.POST.get('product_name')
    description = request.POST.get('description')
    price = request.POST.get('price')
    try:
        img = request.FILES['product_image']
        obj = FileSystemStorage()
        file =obj.save(img.name,img)
    except MultiValueDictKeyError:
        file = ProductDb.objects.get(id=p_id).product_image
    ProductDb.objects.filter(id=p_id).update(category_name=category_name,product_name=product_name,description=description,
                                                 price=price,product_image=file)
    return redirect(display_product)


def delete_product(request,p_id):
    data = ProductDb.objects.filter(id =p_id)
    data.delete()
    return redirect(display_product)

def user_deatils(request):
    data = ContactDb.objects.all()
    return render(request,'user_contacts_deatils.html',{'data':data})



# def update_product(request,p_id):
