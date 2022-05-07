from django.urls import path
from .views import (
    main_view,
    get_json_car_data,
    get_json_model_data,
    create_order,
)

app_name = "orders"

urlpatterns = [
    path('cars', main_view, name='main-view'),
    path('cars-json/', get_json_car_data, name='cars-json'),
    path('models-json/<str:car>/', get_json_model_data, name='models-json'),
    path('create/', create_order, name='create-order'),
]
