from django.db import models

# Create your models here.
class raw_master(models.Model):
    rid=models.AutoField(primary_key=True)
    rname=models.CharField(max_length=30,unique=True)
    
     
    def __str__(self):
        return self.rname
    
class product_master(models.Model):
    pid=models.AutoField(primary_key=True)
    pname=models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.pname
    

class squ_master(models.Model):
    uid=models.AutoField(primary_key=True)
    uname=models.CharField(max_length=30)

    def __str__(self):
        return self.uname
    

class vendor_master(models.Model):
    vname=models.CharField(max_length=30)
    vaddress=models.TextField()
    vphone=models.IntegerField()

    def __str__(self):
        return self.vname

class customer_master(models.Model):
    cname=models.CharField(max_length=30)
    caddress=models.TextField()
    cphone=models.IntegerField()

    def __str__(self):
        return self.cname




class ledger(models.Model):
    raw_m=models.ForeignKey(raw_master,on_delete=models.CASCADE)
    unit=models.ForeignKey(squ_master,on_delete=models.CASCADE)
    quantity=models.FloatField()

    def __str__(self):
        return str(self.raw_m)


class purchase(models.Model):
    rmat=models.ForeignKey(raw_master,on_delete=models.CASCADE)
    Quantity=models.IntegerField()
    unit=models.ForeignKey(squ_master,on_delete=models.CASCADE)
    price=models.FloatField()
    vmat=models.ForeignKey(vendor_master,on_delete=models.CASCADE)
    #payment=models.CharField(max_length=10)
    CHOICES = (
    ('paid','Paid'),
    ('credit','Credit'),
    )
    payment = models.CharField(max_length=6, choices=CHOICES, default='credit')
    #date=models.DateField(auto_now_add=True,default=None)
     
    def __str__(self):
        return str(self.rmat)


class sale(models.Model):
    product=models.ForeignKey(product_master,on_delete=models.CASCADE)
    Quantity=models.IntegerField()
    #unit=models.ForeignKey(squ_master,on_delete=models.CASCADE)
    price=models.FloatField()
    custom=models.ForeignKey(customer_master,on_delete=models.CASCADE)
    #payment=models.CharField(max_length=10)
    CHOICES = (
    ('paid','Paid'),
    ('credit','Credit'),
    )
    payment = models.CharField(max_length=6, choices=CHOICES, default='credit')
    #date=models.DateField(auto_now_add=True,default=None)

    def __str__(self):
        return str(self.product)

    