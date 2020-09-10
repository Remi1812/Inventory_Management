from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# Create your views here.
from django.http import HttpResponse
from .forms import *

def ledgecal(material,un,quan,bool,old_quan):
    try:
        #updating the quantity in the ledger
        ins=ledger.objects.get(raw_m=material,unit=un)
        if bool:
            ins.quantity+=quan
        else:
            ins.quantity-=old_quan
            ins.quantity+=quan    
        ins.save()
    except:
        #creating new instance in ledger
        l=ledger(raw_m=material,unit=un,quantity=quan)
        l.save()
           

def raw(request):
    if request.method=='POST':
        i=request.POST.get('val')
        print(i)
        raw_master.objects.get(rid=i).delete()
        return redirect('raw')
    else:    
        mat=raw_master.objects.all()
        context={'rawm':mat}
        return render(request,'raw_master.html',context)

def product(request):
    if request.method=='POST':
        i=request.POST.get('val')
        print(i)
        product_master.objects.get(pid=i).delete()
        return redirect('product')
    else:    
        mat=product_master.objects.all()
        context={'rawm':mat}
        return render(request,'product.html',context)


def index(request):
    if request.method=='POST':
        form=raw_d(request.POST)
        if form.is_valid():
            material=(form.cleaned_data['rmat'])
            un=(form.cleaned_data['unit'])
            quan=(form.cleaned_data['Quantity'])
            ledgecal(material,un,quan,True,None)
            form.save()
        else:
            return HttpResponse("not valid data")
        return redirect('index')
    else:        
        form=raw_d()
        context={'form':form}
        return render(request,'main.html',context)

def adraw(request):
    if request.method == 'POST':
        r=request.POST.get('rname')
        updated_request = request.POST.copy()
        #changing letters to small to avoid duplicate datas
        updated_request.update({'rname':r.lower()})
        form=raw_m(updated_request)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse("Raw material Already Exists")
            return redirect('addraw')

    else:
        form=raw_m()
        context={'form':form}
        return render(request,'raw.html',context)

def adunit(request):
    if request.method == 'POST':
        r=request.POST.get('uname')
        updated_request = request.POST.copy()
        #changing letters to small to avoid duplicate datas
        updated_request.update({'uname':r.lower()})
        form=squ_m(updated_request)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse("Unit Already Exists")
            return redirect('addraw')

    else:
        form=squ_m()
        context={'form':form}
        return render(request,'raw.html',context)

     

def advendor(request):
    if request.method == 'POST':
        r=request.POST.get('vname')
        updated_request = request.POST.copy()
        #changing letters to small to avoid duplicate datas
        updated_request.update({'vname':r.lower()})
        form=ven_m(updated_request)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse("Vendor Already Exists")
            return redirect('advendor')

    else:
        form=ven_m()
        context={'form':form}
        return render(request,'raw.html',context)

def adcustomer(request):
    if request.method == 'POST':
        r=request.POST.get('cname')
        updated_request = request.POST.copy()
        #changing letters to small to avoid duplicate datas
        updated_request.update({'cname':r.lower()})
        form=cus_m(updated_request)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse("customer Already Exists")
            return redirect('adcustomer')

    else:
        form=cus_m()
        context={'form':form}
        return render(request,'raw.html',context)


def deletepur(request,did):
    ins=purchase.objects.get(id=did)
    led_ins=ledger.objects.get(raw_m=ins.rmat,unit=ins.unit)
    led_ins.quantity-=ins.Quantity
    print(led_ins.quantity)
    led_ins.save()
    if led_ins.quantity == 0:
        led_ins.delete()
    ins.delete()    
    return redirect('purchaserec')

def prod(request):
    if request.method == 'POST':
        r=request.POST.get('pname')
        updated_request = request.POST.copy()
        #changing letters to small to avoid duplicate datas
        updated_request.update({'pname':r.lower()})
        form=pro_m(updated_request)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse("Product Already Exists")
            return redirect('advendor')

    else:
        form=pro_m()
        context={'form':form}
        return render(request,'prod.html',context)

def ledgers(request):
    obj=ledger.objects.all()
    
    return render(request,'ledg.html',{'items':obj})
     
def saless(request):
    if request.method=='POST':
        form=sales(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse("not valid data")
        return redirect('salerec')
    else:        
        form=sales()
        context={'form':form}
        return render(request,'sales.html',context)

   
def salerec(request):
    obj=sale.objects.all()
    return render(request,'salerecord.html',{'items':obj})

def purchaserec(request):
    obj=purchase.objects.all()
    return render(request,'purcrecord.html',{'items':obj})
    
def editpur(request,eid):
    p=purchase.objects.get(id=eid)
    if request.method=='POST':
        form=raw_d(request.POST)
        if form.is_valid():
            ledgecal(form.cleaned_data['rmat'],form.cleaned_data['unit'],form.cleaned_data['Quantity'],False,p.Quantity)
            p.rmat=form.cleaned_data['rmat']
            p.Quantity=form.cleaned_data['Quantity']
            p.unit=form.cleaned_data['unit']
            p.price=form.cleaned_data['price']
            p.vmat=form.cleaned_data['vmat']
            p.payment=form.cleaned_data['payment']
            p.save()
            return redirect('purchaserec')
        else:
            print("Not valid data")    
    else: 
        form=raw_d(instance=p)
    return render(request,'editpur.html',{'pform':form})