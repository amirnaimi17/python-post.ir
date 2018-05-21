# Create your tasks here
from __future__ import absolute_import, unicode_literals

import requests
from django.conf import settings
from zeep import Client
from xml.etree import ElementTree as ET

from .data import make_envelope
from .celery import app


@app.task(name='generate_barcode_task', bind=True)
def generate_barcode_task(self, validated_data):
    city_code = validated_data.get('CityCode')
    type_code = validated_data.get('TypeCode')

    client = Client(settings.POST_GET_BARCODE_URL)
    result = client.service.getMassBarcode24(validated_data['UserName'], validated_data['Password'],
                                             settings.POST_NODE_CODE,
                                             city_code,
                                             type_code)

    return result


@app.task(name='calculate_price_task', bind=True)
def calculate_price_task(self, validated_data):
    client = Client(settings.POST_CALCULATE_PRICE_SERVICE_URL)
    result = client.service.CalculatePrice(validated_data)

    return result


@app.task(name='constant_contract_parcel_task', bind=True)
def constant_contract_parcel_task(self, validator):
    contract_code = validator.get('contract_code')
    barcode = validator.get('barcode')
    post_node_code = validator.get('post_node_code')
    destination_code = validator.get('destination_code')
    parcel_type = validator.get('parcel_type')
    sender_name = validator.get('sender_name')
    receiver_name = validator.get('receiver_name')
    parcel_accept_date = validator.get('parcel_accept_date')
    parcel_accept_time = validator.get('parcel_accept_time')
    receiver_postal_code = validator.get('receiver_postal_code')
    sender_postal_code = validator.get('sender_postal_code')
    additional_info = validator.get('additional_info')
    sender_national_code = validator.get('sender_national_code')
    receiver_national_code = validator.get('receiver_national_code')

    dataset = [contract_code, barcode, post_node_code, destination_code, parcel_type, sender_name, receiver_name,
               parcel_accept_date, parcel_accept_time, receiver_postal_code, sender_postal_code,
               additional_info, sender_national_code, receiver_national_code]

    client = Client(settings.POST_CONTRACT_URL)
    response = client.service.PushConstContractParcels(dataset, settings.POST_USERNAME, settings.POST_PASSWORD)

    if response is None:
        return 'success'
    else:
        return response


@app.task(name='variable_contract_parcel_task', bind=True)
def variable_contract_parcel_task(self, validator):

    xml_data = make_envelope(**validator)
    response = requests.post(settings.POST_CONTRACT_URL, data=xml_data, headers={'Content-Type': 'text/xml'})

    if response.status_code == 200:
        return 'success'
    else:
        return 'error'


@app.task(name='get_city_task', bind=True)
def get_city_task(self, validated_data):
    type = validated_data.get('type')

    client = Client(settings.POST_GET_BARCODE_URL)
    with client.options(raw_response=True):
        response = client.service.getcity(validated_data['UserName'], validated_data['Password'], type)

    xml = ET.fromstring(response.text)
    et = ET.ElementTree(xml)

    dict_data = {}

    if type == 0:
        dict_data = list(
            map(lambda x: {'PNAME': x.findall('PNAME')[0].text, 'ENAME': x.findall('ENAME')[0].text,
                           'CODE': x.findall('CODE')[0].text}, et.iter('Table')))
    if type == 1:
        dict_data = list(
            map(lambda x: {'State_Code': x.findall('State_Code')[0].text, 'Pname': x.findall('Pname')[0].text,
                           'Ename': x.findall('Ename')[0].text, 'CenterFlag': x.findall('CenterFlag')[0].text,
                           'code': x.findall('code')[0].text}, et.iter('Table')))
    if type == 2:
        dict_data = list(
            map(lambda x: {'PNAME': x.findall('PNAME')[0].text, 'ENAME': x.findall('ENAME')[0].text,
                           'CITY_CODE': x.findall('CITY_CODE')[0].text,
                           'ISACTIVE': x.findall('ISACTIVE')[0].text,
                           'CODE': x.findall('CODE')[0].text}, et.iter('Table')))

    if type == 3:
        dict_data = list(
            map(lambda x: {'PNAME': x.findall('PNAME')[0].text, 'ENAME': x.findall('ENAME')[0].text,
                           'GROUP_CODE': x.findall('GROUP_CODE')[0].text,
                           'CODE': x.findall('CODE')[0].text}, et.iter('Table')))

    return dict_data