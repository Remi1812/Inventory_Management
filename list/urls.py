from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('raw',views.raw,name='raw'), 
    path('product',views.product,name='product'), 
    path('adraw',views.adraw,name='addraw'),
    path('adunit',views.adunit,name='adunit'),
    path('adprod',views.prod,name='adprod'),
    path('advendor',views.advendor,name='advendor'),
    path('adcustomer',views.adcustomer,name='adcustomer'),
    path('sale',views.saless,name='sale'),
    path('deletepur<int:did>',views.deletepur,name='deletepur'), 
    path('editpur<int:eid>',views.editpur,name='editpurchase'),
    path('purchaserec',views.purchaserec,name='purchaserec'),
    path('salerec',views.salerec,name='salerec'),
    path('ledger',views.ledgers,name='ledger'),
    
]