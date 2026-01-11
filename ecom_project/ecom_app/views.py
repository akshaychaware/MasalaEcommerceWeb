from genericpath import exists
from random import randrange

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from .models import *

try:
    import razorpay # type: ignore
except ImportError:
    razorpay = None

# Create your views here.


def home(request):
   context={}
   sup=Masala.objects.all()
   
   context['product']=sup
   return render(request,'index.html',context)




def user_login(request):

    if request.method == 'POST':
        uname = request.POST.get('uname')
        upsw = request.POST.get('upsw')
        context={}
        if uname=="" or upsw=="":
            context['errormsg']="fields cannot be empty.."
            return render(request,'login.html',context)
        else:
            u=authenticate(username=uname,password=upsw)
            #print(u)
            if u is not None:
                login(request,u)    
                return redirect('index')
            else:
                context['errormsg']="Invalid username and password.."
                return render(request,'login.html',context)            
    else:
        return render(request,'login.html')
    

def user_register(request):

    if request.method == 'POST':
        uname = request.POST.get('uname')
        upsw = request.POST.get('upsw')
        uemail = request.POST.get('uemail')
        ucpsw = request.POST.get('ucpsw')
        context={}
        if uname=="" or upsw=="" or ucpsw=="" or uemail=="" :
            context['errormsg']="fields cannot be empty.."
            return render(request,'register.html',context)
        elif upsw != ucpsw:
            context['errormsg']="password and confirm password didn't match.."
            return render(request,'register.html',context)
        else:  
            try:  
                u = User.objects.create(username=uname, password=upsw,email=uemail)
                u.set_password(upsw)       
                u.save()
                context['success']="User created successfully"
                return render(request, 'register.html',context)
            except Exception:
                context['errormsg']="user with same username already present.."
                return render(request,'register.html',context)
    else:
        return render(request,'register.html')



def user_logout(request):
    logout(request)
    return redirect('index')


def product_details(request , pid):

    context = {}
    p =  Masala.objects.get(id = pid)
    context['product'] = p
    # print(m)

    return render(request , 'product_details.html' , context)

def addtocart(request, pid):
    if not request.user.is_authenticated:
        return redirect('login')

    context = {}
    user = request.user
    product = Masala.objects.get(id=pid)
    
    context['product'] = product

    # Check if the product is already in the cart
    exists = cart.objects.filter(uid=user, pid=product).exists()

    if exists:
        context['errmsg'] = "This Product is already in your Cart !!"
    else:
        cart.objects.create(uid=user, pid=product)
        context['success'] = "Product added to Your Cart Successfully!"

    return render(request, "product_details.html", context)


def cartt(request):
    context={}
    t=0
    uid=request.user.id
    c=cart.objects.filter(uid=uid)
    np=len(c)
    for p in c:
        t=t+p.pid.prize*p.qty # type: ignore
    context['Masala']=c
    context['n']=np
    context['total']=t
    return render(request,'cart.html',context)


def updateqty(request,qv,cid):
    cart_items=cart.objects.filter(id=cid)
    if not cart_items:
        return redirect('cartt')
    
    cart_item=cart_items[0]   #get the single cart object

    if qv=='1':
        #increase quantity by 1
        cart_item.qty=cart_item.qty+1
        cart_item.save()
    else:
        if cart_item.qty > 1:
            cart_item.qty=cart_item.qty - 1
            cart_item.save()
    return redirect('cartt')

def removepc(request,cid):
    c=cart.objects.filter(id=cid)
    c.delete()
    return redirect('cartt')


def placeorder(request):
    context = {}
    userid = request.user.id
    c = cart.objects.filter(uid=userid)
    print(c)
    oid = randrange(1000, 99909)
    for x in c:
        o = order.objects.create(order_id=oid, pid=x.pid, uid=x.uid, qty=x.qty)
        o.save()
        x.delete()

    orders = order.objects.filter(uid=request.user.id, order_id=oid)
    context['products'] = orders
    np = len(orders)
    s = 0
    for p in orders:
        s = s + p.pid.prize * p.qty # type: ignore
    context['total'] = s
    context['n'] = np     

    return render(request, "place_order.html", context)



def pay(request):
    context = {}
    s = 0

    orders = order.objects.filter(uid=request.user.id).order_by('-order_id')

    if orders:
        oid = orders[0].order_id  
        orders = order.objects.filter(uid=request.user.id, order_id=oid)

        for p in orders:
            s = s + p.pid.prize * p.qty # type: ignore
            print(s)

        client = razorpay.Client(auth=("rzp_test_RTGbk96sQcEcoy", "YN3eqOZMp7bAAGzI7cVJnxvd")) # type: ignore
        data = { "amount": s*100, "currency": "INR", "receipt": "order_rcptid_" + str(oid) }
        payment = client.order.create(data=data) # type: ignore
        print(payment)
        context['data'] = payment

    return render(request, 'pay.html', context)






# views.py
# from .models import Add_product

def add_ingredient(request):
    context={}
    if not request.user.is_authenticated:
        return redirect('login')
    
    context={}
    
    if request.method == 'POST':
        
   
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        unit = request.POST.get('unit')
        prize = request.POST.get('prize')
        mrp = request.POST.get('mrp')
        discount = request.POST.get('discount')
        note = request.POST.get('note')
        ingredients = request.POST.get('ingredients')
        recipe = request.POST.get('recipe')
        img = request.FILES.get('image')
        # Save in database
        exists = Masala.objects.filter(name=name).exists()
        if exists:
            context['errormsg'] = "This ingredient is already added..!!!"
        else:
            Masala.objects.create(
                name=name,
                quantity=quantity,
                unit=unit,
                prize=prize,
                mrp=mrp,
                discount=discount,
                note=note,
                ingredients=ingredients,
                recipe=recipe,
                img=img
            )
            context['success'] = "Ingredient added successfully!"

    return render(request, 'add_ingredients.html', context)



# search Product

def index(request):
    query = request.GET.get('q')
    if query:
        products = Masala.objects.filter(name__icontains=query)
    else:
        products = Masala.objects.all()

    context = {'suppliment': products, 'query': query}
    return render(request, 'index.html', context)
