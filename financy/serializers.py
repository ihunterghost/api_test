from rest_framework import serializers
from .models import *

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class ExpensesTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpensesType
        fields = '__all__'

class EarningsTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EarningsType
        fields = '__all__'

class ExpensesSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(many=False, queryset=ExpensesType.objects.all(), slug_field='category')
    account = serializers.SlugRelatedField(many=False, queryset=Account.objects.all(), slug_field='name')
    payment = serializers.SlugRelatedField(many=False, queryset=Payment.objects.all(), slug_field='type')
    class Meta:
        model = Expenses
        fields = ['description', 'category', 'account', 'payment', 'value']

class EarningsSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(many=False, queryset=EarningsType.objects.all(), slug_field='category')
    account = serializers.SlugRelatedField(many=False, queryset=Account.objects.all(), slug_field='name')
    payment = serializers.SlugRelatedField(many=False, queryset=Payment.objects.all(), slug_field='type')
    class Meta:
        model = Earnings
        fields = ['description', 'category', 'account', 'payment', 'value']