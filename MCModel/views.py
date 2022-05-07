from django.shortcuts import render
from .models import Car, Model, Order
from django.http import JsonResponse


def main_view(request):
    qs = Car.objects.all()
    return render(request, 'cmodel/car.html', {'qs': qs})


# send car objects
def get_json_car_data(request):
    qs_val = list(Car.objects.values())
    print(qs_val)
    print(type({'data': qs_val}))
    return JsonResponse({'data': qs_val})  # dictionary as a response


# send model objects
def get_json_model_data(request, *args, **kwargs):
    selected_car = kwargs.get('car')
    obj_models = list(Model.objects.filter(car__name=selected_car).values())
    return JsonResponse({'data': obj_models})


def create_order(request):
    if request.method == "POST":
        car = request.POST.get('car')
        car_obj = Car.objects.get(name=car)
        model = request.POST.get('model')
        model_obj = Model.objects.get(name=model, car__name=car_obj.name)
        Order.objects.create(car=car_obj, model=model_obj)
        return JsonResponse({'created': True})
    return JsonResponse({'created': False})
