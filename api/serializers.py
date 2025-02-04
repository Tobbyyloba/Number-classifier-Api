from rest_framework import serializers

class ClassifyNumbersSerializers(serializers.Serializer):
    number = serializers.IntegerField()
    is_prime = serializers.BooleanField()
    is_perfect = serializers.BooleanField()
    properties = serializers.ListField(child=serializers.CharField())
    digit_sum = serializers.IntegerField()
    fun_fact = serializers.CharField()