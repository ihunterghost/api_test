from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import *
from financy.views import *

router = routers.DefaultRouter()
router.register(r'api/log', LogViewSet)
router.register(r'api/events', EventsViewSet)
router.register(r'api/appis/device', DeviceViewSet)
router.register(r'api/appis/condominium', CondominiumViewSet)
router.register(r'api/financy/account', AccountViewSet)
router.register(r'api/financy/payment', PaymentViewSet)
router.register(r'api/financy/expensestype', ExpensesTypesViewSet)
router.register(r'api/financy/earningstype', EarningsTypesViewSet)
router.register(r'api/financy/expenses', ExpensesViewSet)
router.register(r'api/financy/earnings', EarningsViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('user.urls')),
    path('admin/', admin.site.urls)
]