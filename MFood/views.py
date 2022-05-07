from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.shortcuts import render
from .forms import OrderForm, UserRegistrationForm, FoodForm
from .models import Category, Food, OrderFood
from django.contrib import messages
import time, datetime


def search_engine(request):
        response = None  #begin with this
        keyword  =request.POST.get("keyword")
        print(keyword)
        queryset = Food.objects.filter(name__icontains = keyword)
        print(queryset)
        if len(queryset) > 0 and len(keyword) > 0:
            customer_list = [] #inititae an empty list
            
            #Append all customer obj into the list using loop.
            for obj in queryset:
                item= {
                    'pk': obj.id,
                    'name': obj.name 
                }
                customer_list.append(item)
            
            #now attach customer_list  to the response
            response = customer_list    
        else:
            response = "Sorry, We don't currently have "+str(keyword)    
            print(response)
        
        return JsonResponse({'data':response})    

def dashboard_view(request):
    registrationform = UserRegistrationForm()
    food_queryset = Food.objects.all()
    print(food_queryset)
    orderfood_queryset = OrderFood.objects.all()
    foodform = FoodForm()
    orderform =OrderForm
    context={
        'registrationform':registrationform,
        'foodform': foodform,
        'orderform': orderform,
        'food_queryset':food_queryset,
        'orderfood_queryset':orderfood_queryset,
        }
    return render(request, 'main.html', context)


def foodcreate_view(request):
    if request.method == "POST":
        foodform = FoodForm()
        foodform = FoodForm(request.POST)
        food_queryset={}
        action = ''
        if foodform.is_valid():       
            get_id=request.POST['sid']
            get_name = request.POST['name']
            category = request.POST['category']
            get_price = request.POST['price']
            added_by = request.POST['added_by']
            get_added_on = request.POST['added_on']  
            get_updated_on = request.POST['updated_on']
            get_added_by =User.objects.get(id=added_by)
            get_category = Category.objects.get(id=category)


            if get_id:
                food_obj = Food(id=get_id,name=get_name, category= get_category, price = get_price, added_by=get_added_by, added_on=get_added_on, updated_on = get_updated_on  )
                food_obj.save()
                action = 'update'
                print("Updated ",food_obj)
                food_queryset=list(Food.objects.values()) 
                print('-----------------------')
                for i in  list(Food.objects.values()):
                    if i['added_on']:
                        c = i['added_on']
                        i['added_on']=int(time.mktime(c.timetuple())) * 1000

            else:
                food_obj = Food(name=get_name, category= get_category, price = get_price, added_by=get_added_by, added_on=get_added_on, updated_on = get_updated_on  )
                food_obj.save()
                action = 'create'
                print("Created ",food_obj)
                food_queryset=list(Food.objects.values()) 
                print('-----------------------')
                for i in  food_queryset:
                    if i['added_on']:
                        c = i['added_on']
                        i['added_on']=int(time.mktime(c.timetuple())) * 1000
                        print(i['added_on'])

        else:
            messages.error(request, "All fields are mandatory!.")
            return JsonResponse(
                                  {'status':'error',
                                 })

        return JsonResponse({'status':action,
                            'food_queryset':food_queryset, })
    else:
        return JsonResponse({'status':0})




def fooddelete_view(request):
    registrationform = UserRegistrationForm()
    if  request.method =="POST":
        getid=int(request.POST['id'])
        print(getid)
        food_obj=Food.objects.get(id=getid)
        print('Obj:',food_obj)
        food_obj.delete()
        
        foodvalues = Food.objects.values()
        foodlist = list(foodvalues)
        return JsonResponse({
                'action':'delete',
                'food_queryset':foodlist })
    else:
        return JsonResponse({
                'status':0,
               } )


def foodupdate_view(request):
    if request.is_ajax() and request.method =="POST":
        getid=int(request.POST['id'])
        print(getid)
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
            "updated_on": food_obj.updated_on,
            "added_by": food_obj.added_by.username,
             'action':'update',
        }
        print(food_data)
        return JsonResponse(food_data)


def ordercreate_view(request):
    registrationform = UserRegistrationForm()
    foodform = FoodForm()
    orderform =OrderForm
    if request.method == "POST" and request.is_ajax():
        orderform = OrderForm(request.POST)
        if orderform.is_valid():     
            getfoodId=int(request.POST['order'])
            order_obj = Food.objects.get(id=getfoodId)
            
            getuserId= request.POST['ordered_by']
            ordered_by = User.objects.get(id=getuserId)
            getstatus =request.POST['status']
            
            orderfood_obj=OrderFood(order=order_obj, ordered_by=ordered_by, status=getstatus)
            orderfood_obj.save()
            print('Orderfood_obj:',orderfood_obj)  

            ordervalues = OrderFood.objects.values()
            print('\n')
            orderlist = list(ordervalues)
            for i in orderlist:
        
                  orderobj=Food.objects.get(id=i['order_id'])
                  i['order_id'] =orderobj.name
                  
                  userobj=User.objects.get(id=i['ordered_by_id'])
                  i['ordered_by_id'] =userobj.username

            print(orderlist)
            
            return JsonResponse({
                'status':1,
                'order_queryset':orderlist })

