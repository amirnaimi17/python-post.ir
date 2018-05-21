from django.test import TestCase


from .serializer import CalculatePriceSerializer
from .tasks import calculate_price_task, get_city_task, generate_barcode_task


class TestCamelCaseConverter(TestCase):

    def test_calculate_price(self):

        kwargs = {"Weight": 2000,  "ParcelType": 1, "ParcelServiceType": 1}

        validator = CalculatePriceSerializer(data=kwargs)
        self.assertEqual(True, validator.is_valid())

        result = calculate_price_task(**validator.validated_data)
        total_amount = result.get('OutTotalAmount')
        self.assertNotEqual(total_amount, 0)

    def test_get_city(self):

        result = get_city_task(type=1)
        self.assertNotEqual(result, {})

    def test_generate_barcode(self):

        result = generate_barcode_task(city_code=1, type_code='12')

        self.assertNotEqual(result, None)
