from django.urls import path

from . import views

app_name = 'barcode'

urlpatterns = [

    path(r'calculate_price', views.CalculatePrice.as_view(), name='calculate_price'),
    path(r'constant_contract_parcel', views.ConstantContractParcel.as_view(), name='constant_contract_parcel'),
    path(r'variable_contract_parcel', views.VariableContractParcel.as_view(), name='variable_contract_parcel'),
    path(r'generate_barcode', views.GenerateBarcode.as_view(), name='generate_barcode'),
    path(r'get_city', views.GetCity.as_view(), name='get_city'),

]
