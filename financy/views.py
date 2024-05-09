from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class ExpensesTypesViewSet(viewsets.ModelViewSet):
    queryset = ExpensesType.objects.all()
    serializer_class = ExpensesTypesSerializer

class EarningsTypesViewSet(viewsets.ModelViewSet):
    queryset = EarningsType.objects.all()
    serializer_class = EarningsTypesSerializer

class ExpensesViewSet(viewsets.ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer

class EarningsViewSet(viewsets.ModelViewSet):
    queryset = Earnings.objects.all()
    serializer_class = EarningsSerializer