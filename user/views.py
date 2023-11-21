from django.shortcuts import render,redirect
from user.models import *
from django.contrib import messages

def index(request):
    return render(request,'index.html')
def register(request):
    return render(request,'register.html')    
def registerAction(request):
    name=request.POST['name']
    Address=request.POST['address']
    Gender=request.POST['gender']
    Username=request.POST['Username']
    Password=request.POST['Password']
    user=Register_tb(Name=name,Address= Address,Gender=Gender,Username=Username,Password=Password)
    user.save()
    messages.add_message(request,messages.INFO,'Registration Succesfull')
    return redirect('register')
def login(request):
    return render(request,'login.html')    
def loginAction(request):
    Username=request.POST['username']
    Password=request.POST['password']
    user=Register_tb.objects.filter(Username=Username,Password=Password)
    if user.count()>0:
        request.session['id']=user[0].id
        return render(request,'userhome.html')
    else:
        messages.add_message(request,messages.INFO,'Login failed')
        return redirect('index')
def viewuser(request):
    user=Register_tb.objects.all()
    return render(request,'viewuser.html',{'vi':user})
def delete(request,id):
    delt=Register_tb.objects.filter(id=id).delete()
    return redirect('viewuser')    
def edit(request,id):
    e=Register_tb.objects.filter(id=id)
    return render(request,"edit.html",{'ed':e})
def editAction(request):
    id=request.POST['id']
    name=request.POST['name']
    address=request.POST['address']
    gender=request.POST['gender']
    username=request.POST['Username']
    newuser=Register_tb.objects.filter(id=id).update(Name=name,Address=address,Gender=gender,Username=username)
    return redirect('viewuser')
def imageupload(request):
    return render(request,'imageupload.html')
def imageAction(request):
    if len(request.FILES)>0:
        img=request.FILES['file']
    else:
        img="no photo"
    image=image_tb(File=img)
    image.save()
    return redirect('imageupload') 
def viewimage(request):
    image=image_tb.objects.all()
    return render(request,'viewimage.html',{'im':image})  
def dropdownbinding(request):
    country=country_tb.objects.all()
    return render(request,'dropdownbinding.html',{'co':country})            
def getstate(request):
    cid=request.GET['co'] 
    state=state_tb.objects.filter(countryid=cid)
    return render(request,'getstate.html',{'sta':state})    
def jquerylink(request):
    return render(request,'jquerylink.html')
def educationdetails(request):
    return render(request,'educationdetails.html')    









   