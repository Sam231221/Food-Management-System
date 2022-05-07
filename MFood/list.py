list=[
    {'name':'samir',
       'age':21
       },
    {'name':'sama',
       'age':22
       },
      ]
for i in list:
    i['name'] = 'ocky'
    
print(list)    


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
