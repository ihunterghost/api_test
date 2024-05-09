"""
URL configuration for api_test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import *
from financy.views import *

router = routers.DefaultRouter()
router.register(r'log', LogViewSet)
router.register(r'appis/device', DeviceViewSet)
router.register(r'appis/condominium', CondominiumViewSet)
router.register(r'financy/account', AccountViewSet)
router.register(r'financy/payment', PaymentViewSet)
router.register(r'financy/expensestype', ExpensesTypesViewSet)
router.register(r'financy/earningstypes', EarningsTypesViewSet)
router.register(r'financy/expenses', ExpensesViewSet)
router.register(r'financy/earnings', EarningsViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]