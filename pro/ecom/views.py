# from django.shortcuts import render, HttpResponse, redirect
# from .models import *

# # Create your views here.

# def first(request):
#     return HttpResponse('this is first page..')

# def demo(request):
#     return render(request, 'demo.html')

# def style(request):
#     return render(request, 'style.html')

# def show(request):
#     data = Student.objects.all()
#     return render(request, 'show.html',{'student': data})

# def showimg(request):
#     dataimg = Img.objects.all()
#     return render(request, 'showimg.html', {'dataimg': dataimg})

# def store(request):
#     if request.method == 'POST':
#         store_data = Student()
#         store_data.email = request.POST.get('email')
#         store_data.name = request.POST.get('uname')
#         store_data.save()
#     return render(request, 'store.html')

# def storeget(request):
#     store_data = Student()
#     store_data.email = request.GET.get('email')
#     store_data.name = request.GET.get('uname')
#     store_data.save()
#     return render(request, 'storeget.html')

# def storeimg(request):
#     if request.method == 'POST' and request.FILES:
#         store_image = Img()
#         store_image.name = request.POST['name']
#         store_image.image = request.FILES['image']
#         store_image.save()
#     return render(request,'storeimg.html')

# # filter - return multiple matching quries
#     # - if query not found, it does not give error

# # get - return single matching query
#     # - if query not found, it gives error



# def register(request):
#     if request.method == 'POST':
#         sign_up = Registration(email=request.POST['email'], 
#                                name=request.POST['name'],
#                                mob=request.POST['mob'],
#                                add=request.POST['add'], 
#                                password=request.POST['password'])
#         try:
#             already_reg = Registration.objects.get(email=request.POST['email'])
#             if already_reg:
#                 return render(request, 'register.html', {'already': 'already registered'})
#         except:
#             sign_up.save()
#             return render(request, 'register.html',{'registration':'successfully done'})
    
#     else:
#         return render(request, 'register.html')
    
# def login(request):
#     if request.method == 'POST':
#         try:
#             is_present = Registration.objects.get(email=request.POST['email'])
#             if is_present:
#                 if request.POST['password'] == is_present.password:
#                    request.session['login'] = is_present.email
#                    # return HttpResponse('Login successful')
#                    return redirect('index')
                
#                 else:
#                     return render(request, 'login.html', {'wrong_pass': 'Incorrect password'})
#         except:
#             return render(request, 'login.html', {'not_registered': 'Email not found'})
#     else:        
#         return render(request, 'login.html')

# def profile(request):
#     if 'login' in request.session:
#         logged_user=Registration.objects.get(email = request.session['login'])
#         if request.method == 'POST':
#             logged_user.name = request.POST.get('name')
#             logged_user.add = request.POST.get('add')   
#             logged_user.mob = request.POST.get('mob')
#             logged_user.save()
#             # return render(request, 'profile.html', {'logged_in': True, 'logged_user': logged_user})
#             return redirect('profile')
#         else:
#             return render(request, 'profile.html', {'logged_in': True, 'logged_user': logged_user})    
#     else:
#         return redirect('login')

# def index(request):
#     cat = category.objects.all()
#     if 'login' in request.session:   
#     # cat = category.objects.filter(name = 'rrr') 
#     # cat = category.objects.get(name = 'rrr')  
#         return render(request, 'index.html', {'cat': cat,'logged_in':True})
#     else:
#         return render(request, 'index.html', {'cat':cat})

# def logout(request):
#     del request.session['login']
#     return redirect('index')

# def cat_pro(request, id):
#     pro = product.objects.filter(category = id)
#     if 'login' in request.session:
#         return render(request, 'cat_pro.html', {'pro': pro, 'logged_in': True})
#     else:
#         return render(request, 'cat_pro.html', {'pro': pro})
    
# def pro_details(request, id):
#     prod = product.objects.get(pk = id)
#     if 'login' in request.session:
#         if request.method == 'POST':
#             request.session['qty'] = request.POST['qty']
#             request.session['proid'] = id
#             return redirect('checkout')
#         else:
#             return render(request, 'product.html', {'logged_in': True, 'product': prod})
#     else:
#         return render(request, 'product.html', {'product': prod})
    
# def checkout(request):
#     if 'login' in request.session:
#         logged_in = Registration.objects.get(email = request.session['login'])
#         pro = product.objects.get(id = request.session['proid'])
#         if request.method == 'POST':
#             if request.POST['paymentvia'] == 'cod':
#                 obj = order(user= logged_in,
#                             pro = pro,
#                             qty = request.session['qty'],
#                             name = request.POST['name'],
#                             mob = request.POST['mob'],
#                             add = request.POST['add'],
#                             city = request.POST['city'],
#                             state = request.POST['state'],
#                             payment_type = request.POST['paymentvia'],
#                             payment_id = "cod",
#                             total_price = int(request.session['qty']) * pro.price
#                             )
#                 obj.save()
#                 pro.stock -= int(request.session['qty'])
#                 pro.save()
#                 return redirect('index')
#             else:
#                 request.session['amount'] = int(request.session['qty']) * pro.price
#                 return redirect('razorpayment')
#             return render(request, 'checkout.html',{'logged_in': logged_in})

#         else:    
#             return render(request, 'checkout.html',{'logged_in': logged_in})
#     else:
#         return redirect('login')
    

# import razorpay
# from django.conf import settings
# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponseBadRequest

# rozarpay_client = razorpay.Client(auth=(settings.ROZARPAY_KEY_ID, settings.ROZARPAY_KEY_SECRET))

# def razorpayment(request):
#     currency = 'INR'
#     amount = int(request.session['amount']) * 100  
#     razorpay_order = rozarpay_client.order.create(dict(
#         currency=currency,
#         amount=amount,
#         payment_capture='1',
#     ))
#     razorpay_order_id = razorpay_order['id']
#     callback_url = 'http://127.0.0.1:8000/paymenthandler/'
#     return render(request, 'razorpay.html',{razorpay_merchant_key: settings.ROZARPAY_KEY_ID,
#                                             razorpay_amount: amount,
#                                             currency: currency,
#                                             razorpay_order_id: razorpay_order_id,
#                                             callback_url: callback_url})

# @csrf_exempt
# def paymenthandler(request):
#     if request.method == 'POST':
#         try:
#             payment_id = request.POST.get('razorpay_payment_id', '')
#             razorpay_order_id = request.POST.get('razorpay_order_id', '')
#             signature = request.POST.get('razorpay_signature', '')

#             params_dict = {
#                     'razorpay_payment_id': payment_id,
#                     'razorpay_order_id': razorpay_order_id,
#                     'razorpay_signature': signature
#                 }
#             razorpay_client.utility.verify_payment_signature(params_dict)
#             amount = int(request.session['amount']) * 100
#             razorpay_client.payment.capture(payment_id, amount)
#             return redirect('index') 
#         except Exception as e:
#             print(e,"eeeeeeeeeeeee")
#             return HttpResponseBadRequest()
#     else:
#         return HttpResponseBadRequest("Invalid request method")    
            
            

from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
import razorpay

# Initialize Razorpay client
razorpay_client = razorpay.Client(auth=(settings.ROZARPAY_KEY_ID, settings.ROZARPAY_KEY_SECRET))


# ==================== BASIC VIEWS ====================

def first(request):
    return HttpResponse('this is first page..')

def demo(request):
    return render(request, 'demo.html')

def style(request):
    return render(request, 'style.html')


# ==================== STUDENT & IMAGE ====================

def show(request):
    data = Student.objects.all()
    return render(request, 'show.html', {'student': data})

def showimg(request):
    dataimg = Img.objects.all()
    return render(request, 'showimg.html', {'dataimg': dataimg})

def store(request):
    if request.method == 'POST':
        store_data = Student()
        store_data.email = request.POST.get('email')
        store_data.name = request.POST.get('uname')
        store_data.save()
    return render(request, 'store.html')

def storeget(request):
    store_data = Student()
    store_data.email = request.GET.get('email')
    store_data.name = request.GET.get('uname')
    store_data.save()
    return render(request, 'storeget.html')

def storeimg(request):
    if request.method == 'POST' and request.FILES:
        store_image = Img()
        store_image.name = request.POST['name']
        store_image.image = request.FILES['image']
        store_image.save()
    return render(request, 'storeimg.html')


# ==================== AUTH: REGISTER, LOGIN, PROFILE ====================

def register(request):
    if request.method == 'POST':
        sign_up = Registration(
            email=request.POST['email'],
            name=request.POST['name'],
            mob=request.POST['mob'],
            add=request.POST['add'],
            password=request.POST['password']
        )
        try:
            already_reg = Registration.objects.get(email=request.POST['email'])
            if already_reg:
                return render(request, 'register.html', {'already': 'Already registered'})
        except Registration.DoesNotExist:
            sign_up.save()
            # return render(request, 'register.html', {'registration': 'Successfully done'})
            return redirect('login')  
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        try:
            is_present = Registration.objects.get(email=request.POST['email'])
            if request.POST['password'] == is_present.password:
                request.session['login'] = is_present.email
                return redirect('index')
            else:
                return render(request, 'login.html', {'wrong_pass': 'Incorrect password'})
        except Registration.DoesNotExist:
            return render(request, 'login.html', {'not_registered': 'Email not found'})
    return render(request, 'login.html')

def profile(request):
    if 'login' in request.session:
        logged_user = Registration.objects.get(email=request.session['login'])
        if request.method == 'POST':
            logged_user.name = request.POST.get('name')
            logged_user.add = request.POST.get('add')
            logged_user.mob = request.POST.get('mob')
            logged_user.save()
            return redirect('profile')
        return render(request, 'profile.html', {'logged_in': True, 'logged_user': logged_user})
    return redirect('login')


# ==================== INDEX, CATEGORY, PRODUCT ====================

def index(request):
    cat = category.objects.all()
    return render(request, 'index.html', {
        'cat': cat,
        'logged_in': 'login' in request.session
    })

def logout(request):
    request.session.flush()
    return redirect('index')

def cat_pro(request, id):
    pro = product.objects.filter(category=id)
    return render(request, 'cat_pro.html', {
        'pro': pro,
        'logged_in': 'login' in request.session
    })

def pro_details(request, id):
    prod = product.objects.get(pk=id)
    if 'login' in request.session:
        logged_in = Registration.objects.get(email=request.session['login'])
        # if request.method == 'POST':
        if 'buy' in request.POST:
            if int(request.POST['qty']) > prod.stock:
                return render(request, 'product.html',{'logged_in':True,'product':prod,'less_stock':True})
            else:
                request.session['qty'] = request.POST['qty']
                request.session['proid'] = id
                return redirect('checkout')
        elif 'cart' in request.POST:
            add_to_cart = cart(user = logged_in,
             pro = prod,
             qty = request.session['qty'],
             total_price = prod.price * int(request.session['qty'])
             )
            add_to_cart.save()
            return redirect('index')
    # if int(request.POST['qty']) > prod.stock:      
        return render(request, 'product.html', {
        'product': prod,
        'logged_in': 'login' in request.session
    })
# do line or likni hai task 14 m se timr 30:


# ==================== CHECKOUT + PAYMENT ====================

def checkout(request):
    if 'login' in request.session:
        logged_in = Registration.objects.get(email=request.session['login'])
        pro = product.objects.get(id=request.session['proid'])

        if request.method == 'POST':
            qty = int(request.session['qty'])
            total = qty * pro.price
            if request.POST['paymentvia'] == 'cod':
                obj = order(
                    user=logged_in,
                    pro=pro,
                    qty=request.session['qty'],
                    name=request.POST['name'],
                    mob=request.POST['mob'],
                    add=request.POST['add'],
                    city=request.POST['city'],
                    state=request.POST['state'],
                    pin=request.POST['pin'],
                    payment_type=request.POST['paymentvia'],
                    payment_id='cod',
                    total_price=pro.price*int(request.session['qty'])
                )
                obj.save()
                pro.stock -= int(request.session['qty'])
                pro.save()
                return redirect('index')
            else:
                request.session['amount'] = pro.price * int(request.session['qty'])
                # request.session['amount'] = total
                request.session['name'] = request.POST['name']
                request.session['mob'] = request.POST['mob']
                request.session['add'] = request.POST['add']
                request.session['city'] = request.POST['city']
                request.session['state'] = request.POST['state']
                request.session['pin'] = request.POST['pin']
                return redirect('razorpayment')
            return render(request, 'checkout.html', {'logged_in': logged_in})
        else:
            return render(request, 'checkout.html', {'logged_in': logged_in})
    else:    
        return redirect('login')


# ==================== RAZORPAY ====================

def razorpayment(request):
    currency = 'INR'
    amount = int(request.session['amount']) * 100  # Razorpay accepts amount in paisa
    razorpay_order = razorpay_client.order.create(dict(
        currency=currency,
        amount=amount,
        payment_capture='0',
    ))
    razorpay_order_id = razorpay_order['id']
    callback_url = 'http://127.0.0.1:8000/paymenthandler/'

    return render(request, 'razorpay.html', {
        'razorpay_merchant_key': settings.ROZARPAY_KEY_ID,
        'razorpay_amount': amount,
        'currency': currency,
        'razorpay_order_id': razorpay_order_id,
        'callback_url': callback_url
    })


@csrf_exempt
def paymenthandler(request):
    if request.method == 'POST':
        try:
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')

            param_dict = {'razorpay_payment_id' : payment_id,
            'razorpay_order_id' : razorpay_order_id,
            'razorpay_signature' : signature}
            razorpay_client.utility.verify_payment_signature(param_dict)
            amount = int(request.session['amount']) * 100
            razorpay_client.payment.capture(payment_id, amount)
            logged_in = Registration.objects.get(email = request.session['login'])
            pro = product.objects.get(id = request.session['proid'])
            store_order = order(user = logged_in,
                  pro = pro,
                  qty = request.session['qty'],
                  name = request.session['name'],
                  mob = request.session['mob'],
                  add = request.session['add'],
                  city = request.session['city'],
                  state = request.session['state'],
                #   pin = request.session['pin'],
                  total_price = request.session['amount'],
                  payment_type = 'online',
                  payment_id = payment_id
                  )
            store_order.save()
            pro.stock -= int(request.session['qty'])
            pro.save()
            return redirect('index')
        except Exception as e:
            print(e,"eeeeeerrrrrrrrrrooooooorrrrr")
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()
