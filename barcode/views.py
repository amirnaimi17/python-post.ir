from django.conf import settings
from django.http import HttpResponseBadRequest
from parler_rest.fields import TranslatedFieldsField
from parler_rest.serializers import TranslatableModelSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import CalculatePriceSerializer, BarcodeSerializer, VariableContractSerializer, \
    ConstantContractSerializer, GetCitySerializer
from .tasks import variable_contract_parcel_task, generate_barcode_task, constant_contract_parcel_task, \
    calculate_price_task, get_city_task
from .models import StaticTypes


class StaticTypesSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=StaticTypes)

    class Meta:
        model = StaticTypes
        fields = ('type', 'group_type', 'value', 'translations')


class StaticTypesViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = StaticTypesSerializer
    queryset = StaticTypes.objects.all()


class CalculatePrice(APIView):
    def post(self, request):
        validator = CalculatePriceSerializer(data=request.data)
        if not validator.is_valid():
            return HttpResponseBadRequest()

        validator.validated_data['UserName'] = settings.POST_USERNAME
        validator.validated_data['Password'] = settings.POST_PASSWORD
        response = calculate_price_task.delay(validator.validated_data)
        if response is None:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': response})
        try:
            response = response.get(timeout=10).__values__
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': str(e)})

        response.pop('UserName')
        response.pop('Password')

        return Response(data=response, status=status.HTTP_200_OK)


class ConstantContractParcel(APIView):
    def post(self, request):
        validator = ConstantContractSerializer(data=request.data)
        if not validator.is_valid():
            return HttpResponseBadRequest()

        response = constant_contract_parcel_task.delay(validator.validate_data)
        if response is not None:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': response})

        return Response(data={'result': 'success'}, status=status.HTTP_200_OK)


class VariableContractParcel(APIView):
    def post(self, request):
        validator = VariableContractSerializer(data=request.data)
        if not validator.is_valid():
            return HttpResponseBadRequest()

        response = variable_contract_parcel_task.delay(validator.validated_data)
        if response is not None:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': response})

        return Response(data={'result': 'success'}, status=status.HTTP_200_OK)


class GetCity(APIView):
    def post(self, request):
        validator = GetCitySerializer(data=request.data)
        if not validator.is_valid():
            return HttpResponseBadRequest()

        from django.conf import settings

        validator.validated_data['UserName'] = settings.POST_USERNAME
        validator.validated_data['Password'] = settings.POST_PASSWORD

        response = get_city_task.delay(validator.validated_data)
        try:
            dict_data = response.get(timeout=10)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': str(e)})

        return Response(data=dict_data, status=status.HTTP_200_OK)


class GenerateBarcode(APIView):
    def post(self, request):
        validator = BarcodeSerializer(data=request.data)
        if not validator.is_valid():
            return HttpResponseBadRequest()

        validator.validated_data['UserName'] = settings.POST_USERNAME
        validator.validated_data['Password'] = settings.POST_PASSWORD

        try:
            result = generate_barcode_task.delay(validator.validated_data)
            response = result.get(timeout=10)
        except Exception as e:
            return Response(data={'result': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(data={'barcode': response.__values__.get('Barcode')}, status=status.HTTP_200_OK)
