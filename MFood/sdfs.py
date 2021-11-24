from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.shortcuts import render
from .forms import OrderForm, UserRegistrationForm, FoodForm
from .models import Category, Food, OrderFood


def dashboard_view(request):
    registrationform = UserRegistrationForm()
    foodform = FoodForm()
    orderform =OrderForm
    orderfood_queryset = OrderFood.objects.all()
    context={
        'registrationform':registrationform,
        'foodform': foodform,
        'orderform': orderform,
        'orderfood_queryset':orderfood_queryset,
        }
    return render(request, 'base.html', context)


def foodlist_view(request):
    foodlist = list(Food.objects.all().values())
    
    return JsonResponse({'foods':foodlist, })

def fooddetail_view(request):
    registrationform = UserRegistrationForm()
    food_queryset = Food.objects.all()
    foodform = FoodForm()
    orderform =OrderForm
    context={
        'registrationform':registrationform,
        'foodform': foodform,
        'orderform': orderform,
        'food_queryset':food_queryset,
        }
    return render(request, 'food.html', context)


def foodcreate_view(request):
    registrationform = UserRegistrationForm()
    foodform = FoodForm()
    orderform =OrderForm
    if request.method == "POST" and request.is_ajax():
        foodform = FoodForm(request.POST)
        query={}
        if foodform.is_valid():       
            get_id=request.POST['sid']
            print(get_id)
            get_name = request.POST['name']
            print('name:',get_name)
            category = request.POST['category']
            print('category:', category)
            get_price = request.POST['price']
            print('price:',get_price)
            added_by = request.POST['added_by']
            print('id',added_by)

            get_added_by =User.objects.get(id=added_by)
            print(get_added_by)
            get_category = Category.objects.get(id=category)
            print(get_category)
            
            if get_id:
                print('Updtaing')
                food_obj = Food(id=get_id,name=get_name, category= get_category, price = get_price, added_by=get_added_by )
                food_obj.save()
                print(food_obj)
                query={
                    'action':'update'
                }
            else:
                print('Creating...')
                query={
                    'action':'create'
                }


        return JsonResponse(query)
    else:
        return JsonResponse({'status':0})

def fooddelete_view(request):
    registrationform = UserRegistrationForm()
    if request.is_ajax() and request.method =="POST":
        getid=request.POST.get('id')
        print(getid)
        food_obj=Food.objects.get(id=getid)
        food_obj.delete()
        
        foodvalues = Food.objects.values()
        foodlist = list(foodvalues)
        return JsonResponse({
                'action':'delete',
                'food_queryset':foodlist })
    else:
        return JsonResponse({
                'status':0,
               })

def foodupdate_view(request):
    if request.is_ajax() and request.method =="POST":
        getid=int(request.POST.get('id'))
        print(type(getid))
        food_obj=Food.objects.get(id=getid)
        
        print(type(food_obj))
        print(food_obj.category.name)
        
        food_data={
            "id":food_obj.id,
            "name": food_obj.name,
            "price": food_obj.price,
            "category": food_obj.category.name,
            "added_on": food_obj.added_on,
            "added_by": food_obj.added_by.username,
            'action':'update',
        }
        print('dict:',food_data)
        return JsonResponse(food_data)


def ordercreate_view(request):
    registrationform = UserRegistrationForm()
    foodform = FoodForm()
    orderform =OrderForm
    if request.method == "POST" and request.is_ajax():
        orderform = OrderForm(request.POST)
        if orderform.is_valid():       
            print(orderform)
            orderform.save()
        print('\n')
        ordervalues = OrderFood.objects.values()
        print(ordervalues)
        print('\n')
        orderlist = list(ordervalues)
        print(orderlist)
        return JsonResponse({
            'status':1,
            'order_queryset':orderlist })
    else:
        return JsonResponse({'status':0})

def orderdelete_view(request):
    registrationform = UserRegistrationForm()
    if request.is_ajax() and request.method =="POST":
        getid=request.POST.get('id')
        print(getid)
        order_obj=OrderFood.objects.filter(id=getid)
        order_obj.delete()
        
        ordervalues = OrderFood.objects.values()
        orderlist = list(ordervalues)
        return JsonResponse({
                'status':1,
                'order_queryset':orderlist })
    else:
        return JsonResponse({
                'status':0,
               })

def orderupdate_view(request):
    registrationform = UserRegistrationForm()
    foodform = FoodForm()
    orderform =OrderForm
    context={
        'registrationform':registrationform,
        'foodform': foodform,
        'orderform': orderform,
        }
    return render(request, 'foodupdate.html', context)



"""
>>> cd  = Food(name="Co") 
>>> cd.save()

cd  = Food.objects.create(name="Cokei") 
"""