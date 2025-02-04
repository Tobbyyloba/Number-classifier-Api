from django.shortcuts import render
from rest_framework.views import APIView
import requests
from rest_framework.response import Response
from api.serializers import ClassifyNumbersSerializers

# Create your views here.
class ClassifyNumberView(APIView):
    serializer_class = ClassifyNumbersSerializers
    def get(self, request, *args, **kwargs):
        number_params = request.GET.get('number')

        number = int(number_params)

        url = f"http://numbersapi.com/{number_params}/math"
        response = requests.get(url)

        payload = {
            "number": number,
            "is_prime": True,
            "is_perfect": True,
            "properties": [],
            "digit_sum" : 5,
            "fun_fact": response.text
        }

        serializer = self.serializer_class(data=payload)
        if serializer.is_valid():
            return Response(serializer.data)