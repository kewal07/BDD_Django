"""hello_bdd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

# Included for brevity and time; Ideally we should use include
from bdd_customer.views import TransactionListCreateAPIView, CardListCreateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transactions', TransactionListCreateAPIView.as_view(), name='transactions'),
    path('cards', CardListCreateAPIView.as_view(), name='cards')
]

