from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adraw',views.adraw,name='addraw'),
    path('adunit',views.adunit,name='adunit'),
    path('adprod',views.prod,name='adprod'),
    path('advendor',views.advendor,name='advendor'),
    path('adcustomer',views.adcustomer,name='adcustomer'),
    path('sale',views.sale,name='sale'),
    path('salerec',views.salerec,name='salerec'),
    path('ledger',views.ledgers,name='ledger'),
    
]