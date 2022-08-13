from itertools import product
from random import randint
from unicodedata import category
from django.shortcuts import redirect, render
from .models import *
from django.views import View
from django.conf import settings
from django.core.mail import send_mail

titles = {
    'index': 'N-AIR Home',
    'Signup': 'N-AIR Signup',
    'checkout': 'N-AIR Checkout',
    'contact': 'N-AIR Contact',
    'products': 'N-AIR Products',
    'Signin': 'N-AIR Signin',
    'single': 'N-AIR Over-Views',
}

data = {}


def get_cart(request):
    cart_data = cart.objects.filter(user=Master.objects.get(Email=request.session['email']))[::-1]
    cart_count = {
            'cart_items': [],
            'total_cart_price': 0,
        }

    # print(cart_data)

    total_price = 0
    d_charge = 80
    cart_c = 0
    for c in cart_data:
        cart_count['cart_items'].append({'price': c.product.selling_price,'qty': c.quantity,'delivery_charges': d_charge,'total_price': c.product.selling_price * c.quantity , 'shoes_img': c.product.shoes_img, 'id': c.product.id , 'product_name': c.product.title.upper , 'c_size': c.Size, 'cart_c':c.cart_c})
        # print(c.product.id)
        

    # for i in cart_count['cart_items']:
    #     if cart_count['cart_items']:
    #         cart_c+=1
    #     else:
    #         cart_c=0
    # print(f"your totel cart prods{cart_c}")

    for qp in cart_count['cart_items']:
        total_price += qp['total_price']

    if total_price < 200:
        cart_count['total_cart_price'] = total_price + d_charge
        data['d_charges'] = d_charge
    else:
        cart_count['total_cart_price'] = total_price
        data['d_charges'] = 0
    data['cart_count'] = cart_count

    # print(cart_count)

# products view functionality
def index(request):
        # get_cart(request)
        return render(request, 'index.html')

class products_view(View):
    def get(self, request,data):

        title = []
        for t in title:
            title.append({'shorttxt':[0], 'text':[1]})

        # mens category

        if data == 'Men-All-Product':    
            Mprod = Product.objects.filter(category='M')
        elif data == 'Men-Shoes':
            Mprod = Product.objects.filter(category='M').filter(subcategory = 'MS')
        elif data == 'Under-10000':
            Mprod = Product.objects.filter(category='M').filter(selling_price__gt = 10000)
        elif data == 'Below-5000':
            Mprod = Product.objects.filter(category='M').filter(selling_price__lt = 10000)
        elif data == "Men-Bottom-Wear":
            Mprod = Product.objects.filter(category='M').filter(subcategory = 'MB')
        elif data == "Men-Tops-Wear":
            Mprod = Product.objects.filter(category='M').filter(subcategory = 'MT')
        elif data == "Men-Casual-Wear":
            Mprod = Product.objects.filter(category='M').filter(subcategory = 'CC')
        elif data == "Men-Gym-Wear":
            Mprod = Product.objects.filter(category='M').filter(subcategory = 'G')
        #end man category

        # women category
        elif data == 'Women-All-Product':    
            Mprod = Product.objects.filter(category='F')
        elif data == 'Women-Shoes':
            Mprod = Product.objects.filter(category='F').filter(subcategory = 'WS')
        elif data == 'Women-Tops':
            Mprod = Product.objects.filter(category='F').filter(subcategory = 'WT')
        elif data == 'Women-Bottom':
            Mprod = Product.objects.filter(category='F').filter(subcategory = 'WB')
        # end woman category

        # kids category
        elif data == 'Kids-All-Product':
            Mprod = Product.objects.filter(category='K')
        elif data == 'Kids-Shoes':
            Mprod = Product.objects.filter(category='K').filter(subcategory = 'KS')
        elif data == 'kids-Gear':
            Mprod = Product.objects.filter(category='K').filter(subcategory = 'KG')
        elif data == 'kids-Watch':
            Mprod = Product.objects.filter(category='K').filter(subcategory = 'KW')
        elif data == 'kids-T-shirt':
            Mprod = Product.objects.filter(category='K').filter(subcategory = 'KT')
        context={
            "men_products": Mprod , 'items': data
        }
        get_cart(request)
        return render(request, 'products.html', context)
        # end kids category

class CustomerCartProduct(View):
    def post(self,request):
        quentity=request.POST.get('quentity')
        size=request.POST.get('Shoes_Size')
        cart_count=request.POST.get('cart_count')
        product_id=request.POST.get('product_id')
        user=Master.objects.get(Email=request.session['email'])
        exist_product=cart.objects.filter(user=user,product__id=product_id)
        totel_items=len(cart.objects.filter(user=user))
        print(f"totel_pro{totel_items}")
        if exist_product.exists():
            exist_product.update(quantity=quentity)
            exist_product.update(Size=size)
            # exist_product.update(cart_c=cart_count)
        else:
            cart_product=cart.objects.create(user=user,
            product=Product.objects.get(id=product_id),quantity=quentity, Size=size)
            cart_product.save()

        get_cart(request)
        return redirect('checkout')
    
        
def Customer_cart(request):
    return render(request, 'Customer_cart.html', get_cart(request))

class Quick_view(View):
    def get(self, request,pk):
        prod = Product.objects.get(pk=pk)
        context={
            'product': prod
        }
        get_cart(request)
        return render(request, 'single.html',context)

# signup_page functionality
def signup(request): 
    request.session['regi_data'] = {
        'email': request.POST['email'],
        'password': request.POST['password'],
    }
    create_otp(request)  # call otp
    return redirect('otp_page')

# signin_page functionality
def signin(request):
    if request.method == 'POST':
        master = Master.objects.get(Email=request.POST['email'])

        if master.Password == request.POST['password']:
            request.session['email'] = master.Email
            return redirect('profile_page')
        else:
            return render(request,'signin_page.html')

# profile_page functionality
def profile_page(request):
    if 'email' in request.session:
        profile_data(request)
        return render(request, 'profile_page.html', titles)
    return redirect('signin_page')

# profile_data functionality
def profile_data(request):
    master = Master.objects.get(Email=request.session['email'])
    profile = Profile.objects.get(Master=master)
    titles['profile_data'] = profile

# profile update functionality
def profile_update(request):

    master = Master.objects.get(Email=request.session['email'])
    profile = Profile.objects.get(Master=master)

    profile.Fullname = request.POST['full_name']
    profile.Mobile = request.POST['mobile']
    profile.State = request.POST['state']
    profile.City = request.POST['city']
    profile.Address = request.POST['address']
    profile.save()
    return redirect('/')

# otp functionality
def create_otp(request):
    email_to_list = [request.session['regi_data']['email']]

    from_email = settings.EMAIL_HOST_USER

    otp = randint(1000,9999)
    request.session['otp'] = otp

    subject = 'Verification N-Air Nike'
    message = f'One Time Password : {otp}'

    send_mail(subject, message , from_email ,email_to_list)

# otp_verify
def otp_verify(request):
    if request.POST:
        otp = int(request.POST['otp'])
        if otp == request.session['otp']:
            #  if request.method == 'POST':
                master = Master.objects.create(
                Email=request.session['regi_data']['email'], Password=request.session['regi_data']['password'],
                isactive = True
                )
                Profile.objects.create(Master=master)

                # print ("Account verified")

                del request.session['regi_data']
                del request.session['otp']
        else: 
            # print("Invaild OTP")
            return redirect('otp_page')

        return redirect('signin_page')
    else:
        pass

# logout functionality

def logout(request):
    if 'email' in request.session:
        del request.session['email']
    return redirect('signin_page')

def contact(request):
    return render(request, 'contact.html', titles)

def checkout(request):
    get_cart(request)
    return render(request, 'checkout.html', data)

def signup_page(request):
    return render(request, 'signup_page.html', titles)

def signin_page(request):
    return render(request, 'signin_page.html', titles)

def otp_page(request):
    return render(request, 'otp_page.html', titles)

def profile_page(request): 
    return render(request, 'profile_page.html', titles)

def buynow(request): 
    profile = Profile.objects.filter(Master=master)
    cart_items = cart.objects.filter(user=Master.objects.get(Email=request.session['email']))[::-1]
    master = Master.objects.get(Email=request.session['email'])

    product_items = {
        'product_list' : []
    }

    
    total_price = 0
    d_charge = 80
    cart_c = 0

    for p_items in cart_items:
        product_items['product_list'].append({'p_name': p_items.product.title, 'p_qty': p_items.quantity, 'p_total_price': p_items.product.selling_price * p_items.quantity , 'p_size': p_items.Size}) 

    for qp in product_items['product_list']:
        total_price += qp['p_total_price']

    if total_price < 200:
        product_items['total_cart_price'] = total_price + d_charge
        data['d_charges'] = d_charge
    else:
        product_items['total_cart_price'] = total_price
        data['d_charges'] = 0

    data['product_items'] = product_items

    # print(product_items)
    get_cart(request)
    return render(request, 'buynow.html', {'add': profile, 'product_items': product_items})

