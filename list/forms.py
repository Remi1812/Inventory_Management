from django.forms import ModelForm

from .models import *

class raw_d(ModelForm):
    class Meta:
        model=purchase
        fields='__all__'

class raw_m(ModelForm):
    class Meta:
        model=raw_master
        fields='__all__'

class sales(ModelForm):
    class Meta:
        model=sale
        fields='__all__'

class pro_m(ModelForm):
    class Meta:
        model=product_master
        fields='__all__'

class squ_m(ModelForm):
    class Meta:
        model=squ_master
        fields='__all__'

class cus_m(ModelForm):
    class Meta:
        model=customer_master
        fields='__all__'



class ven_m(ModelForm):
    class Meta:
        model=vendor_master
        fields='__all__'
