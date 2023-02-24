from django.shortcuts import render, redirect

from hotspot.forms import HotspotForm
from hotspot.models import Hotspot


# Create your views here.
def index(request):
    return render(request,"index.html")
def contact(request):
    return render(request,"contact.html")
def about(request):
    return render(request,"about.html")
def feature(request):
    return render(request,"feature.html")

def add_item(request):
    hot=Hotspot.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        image=request.POST.get('image')
        dateadded=request.POST.get('date_added')
        yearadded=request.POST.get('year_added')
        hotspot=Hotspot(name=name,desc=desc,image=image,date_added=dateadded,year_added=yearadded)
        hotspot.save()
    return render(request,"add.html",{'hot':hot})

def update(request,id):
    hotspot=Hotspot.objects.get(id=id)
    form=HotspotForm(request.POST or None,request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'hotspot': hotspot, 'form': form})

def delete(request,id):
    if request.method=='POST':
        hotspot=Hotspot.objects.get(id=id)
        hotspot.delete()
        return redirect('/')
    return render(request,"delete.html")

