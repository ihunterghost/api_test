from django.contrib import admin
from .models import *

admin.site.register(Account)
admin.site.register(Payment)
admin.site.register(ExpensesType)
admin.site.register(EarningsType)
admin.site.register(Expenses)
admin.site.register(Earnings)