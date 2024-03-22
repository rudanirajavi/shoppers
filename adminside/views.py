from django.shortcuts import render,redirect
from adminside.models import *


# Create your views here.
def login(request):
    

    if 'login' in  request.POST:
        email=request.POST['email']
        password=request.POST['password']
        page = rgsrform.objects.filter(email=email,password=password)
        if page.count()==1:
            row = page.get()
            request.session['page_id']=row.id
            print(page.count())
            msg="valid"
            return redirect('/dashboard')
        else:
            msg="invalid  email or password"
        
       
    return render(request,'login.html')

def register(request):
    rgsr = rgsrform.objects.all()
    obj= rgsrModelForm()
    if 'save' in request.POST:
       
        obj = rgsrModelForm(request.POST,request.FILES)
        if obj.is_valid():
            obj.save()
        return redirect('/login')   
   
    return render(request,'register.html',{'form':obj,'rgsrform':rgsr})
def delete(request,del_id):
    print("ID=",del_id)
    rgsrform.objects.filter(id=del_id).delete()
    return redirect('/view_data')


def edit_profile(request,edit_id):
    row=rgsrform.objects.filter(id=edit_id).get()

    page_id =  request.session['page_id']
    page = rgsrform.objects.filter(id=page_id).get()
    
    obj= rgsrModelForm()
    if request.method == 'POST':        
        form = rgsrModelForm(request.POST, request.FILES, instance=row)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
    else:
        form = rgsrModelForm(instance=row)

    return render(request,'edit-profile.html',{'form':form,'data':row,'page':page})

def dashboard(request):
    if 'page_id' not in  request.session:
        return redirect('/')

    page_id =  request.session['page_id']

    page = rgsrform.objects.filter(id=page_id).get()

    return render(request,'dashboard.html',{'page':page})


def user_login(request):
    page_id =  request.session['page_id']
    page = rgsrform.objects.filter(id=page_id).get()

    if 'login' in  request.POST:
        email=request.POST['email']
        password=request.POST['password']
        page = contact.objects.filter(email=email,password=password)
        if page.count()==1:
            row = page.get()
            request.session['page_id']=row.id
            print(page.count())
            msg="valid"
            return redirect('/home')
        else:
            msg="invalid  email or password"
    return render(request,'user_login.html',{'page':page})

def logout(request):
    if 'page_id' in request.session:
        del request.session['page_id']
    return redirect('/')

def addadmin(request):
    page_id =  request.session['page_id']
    page = rgsrform.objects.filter(id=page_id).get()
    
    rgsr = rgsrform.objects.all()
    obj= rgsrModelForm()
    if 'save' in request.POST:
       
        obj = rgsrModelForm(request.POST,request.FILES)
        if obj.is_valid():
            obj.save()
        return redirect('/dashboard')  

    return render(request,'addadmin.html',{'page':page,'form':obj,'rgsrform':rgsr})
    
def adminuserdata(request):
    page_id =  request.session['page_id']
    page = rgsrform.objects.filter(id=page_id).get()
   
    data = rgsrform.objects.all()
    return render(request,'admin user data.html',{'page':page,'rows':data})

# def home(request):
#     return render(request,'home.html')


def user_login(request):
    
    if 'login' in  request.POST:
        email=request.POST['email']
        password=request.POST['password']
        page = contact.objects.filter(email=email,password=password)
        if page.count()==1:
            row = page.get()
            request.session['page_id']=row.id
            print(page.count())
            msg="valid"
            return redirect('/home')
        else:
            msg="invalid  email or password"
    return render(request,'user_login.html')