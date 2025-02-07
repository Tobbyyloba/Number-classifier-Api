from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from api.serializers import ClassifyNumbersSerializers

class ClassifyNumberView(APIView):
    serializer_class = ClassifyNumbersSerializers

    def get(self, request, *args, **kwargs):
        number_params = request.GET.get('number')

        if not number_params:
            return Response({"error": True}, status=400)

        try:
            number = int(number_params)
        except ValueError:
            return Response({"error": True}, status=400)

        # Compute properties
        is_prime = self.is_prime(number)
        is_perfect = self.is_perfect(number)
        is_armstrong = self.is_armstrong(number)
        digit_sum = sum(int(digit) for digit in str(abs(number)))
        properties = self.get_properties(number)
        fun_fact = self.get_fun_fact(number)

        payload = {
            "number": number,
            "is_prime": is_prime,
            "is_perfect": is_perfect,
            "is_armstrong": is_armstrong,
            "properties": properties,
            "digit_sum": digit_sum,
            "fun_fact": fun_fact
        }

        serializer = self.serializer_class(data=payload)
        if serializer.is_valid():
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def is_prime(self, num):
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_perfect(self, num):
        """Check if a number is a perfect number."""
        if num < 1:
            return False
        return sum(i for i in range(1, num) if num % i == 0) == num

    def is_armstrong(self, num):
        """Check if a number is an Armstrong number."""
        num_str = str(num)
        num_length = len(num_str)
        return num == sum(int(digit) ** num_length for digit in num_str)

    def get_properties(self, num):
        """Get number properties."""
        properties = []
        if num % 2 == 0:
            properties.append("Even")
        else:
            properties.append("Odd")

        if self.is_armstrong(num):
            properties.append("Armstrong Number")

        return properties

    def get_fun_fact(self, num):
        """Fetch a fun fact from numbersapi.com."""
        url = f"http://numbersapi.com/{num}/math"
        response = requests.get(url)
        return response.text if response.status_code == 200 else "No fun fact available."
