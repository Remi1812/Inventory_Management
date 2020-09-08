from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# Create your views here.
from django.http import HttpResponse
from .forms import *

def index(request):
    if request.method=='POST':
        form=raw_d(request.POST)
        if form.is_valid():
            material=(form.cleaned_data['rmat'])
            un=(form.cleaned_data['unit'])
            quan=(form.cleaned_data['Quantity'])
            try:
                #updating the quantity in the ledger
                ins=ledger.objects.get(raw_m=material,unit=un)
                ins.quantity+=quan
                ins.save()
            except:
                #creating new instance in ledger
                l=ledger(raw_m=material,unit=un,quantity=quan)
                l.save()
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
     
def sale(request):
    if request.method=='POST':
        form=sales(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse("not valid data")
        return redirect('sale')
    else:        
        form=sales()
        context={'form':form}
        return render(request,'sales.html',context)

def salerec(request):
    obj=purchase.objects.all()
    return render(request,'salerecord.html',{'items':obj})
    