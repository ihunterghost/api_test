from django.db import models

class Account(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

class Payment(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.type

class ExpensesType(models.Model):
    type = models.CharField(max_length=20)
    group = models.CharField(max_length=20)
    category = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.category

class EarningsType(models.Model):
    group = models.CharField(max_length=20)
    category = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.category

class Expenses(models.Model):
    description = models.CharField(max_length=50)
    category = models.ForeignKey(ExpensesType, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Earnings(models.Model):
    description = models.CharField(max_length=50)
    category = models.ForeignKey(EarningsType, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
