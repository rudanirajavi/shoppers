from django.shortcuts import render,redirect
from userside.models import *
from django.db.models import Sum


# Create your views here.
def home(request):
    all_slides = sliders.objects.all()
    all_categorie = categories.objects.all()
    all_product = products.objects.all()[:4]
    
    # catagory = categories.objects.filter(id=cat_id).get()
    # catagory_products = products.objects.filter(cat_id=catagory)
    
    # categories 
    pro_cats=categories.objects.all()
    page_id =  request.session['page_id']
    page = contact.objects.filter(id=page_id).get()

    user_id = request.session.get('page_id')
    all_carts = carts.objects.filter(user_id=user_id)
    total_cart = all_carts.aggregate(total=Sum('qty'))['total'] or 0

    all_likes = likes.objects.filter(user_id=user_id)
    total_like = all_likes.aggregate(total=Sum('user_id'))['total'] or 0
    # return render(request,'home.html',{ 'catagory_products': catagory_products, 'catagory': catagory,'total_cart':total_cart,'cat':pro_cats,'sliders':all_slides,'categories':all_categorie,'products':all_product,'page':page})
    return render(request,'home.html',{ 'total_like':total_like,'total_cart':total_cart,'cat':pro_cats,'sliders':all_slides,'categories':all_categorie,'products':all_product,'page':page})

def slider(request):
    slider = sliders.objects.all()
    obj = sliderModelForm()

    if 'save' in request.POST:
        obj=sliderModelForm(request.POST,request.FILES)
        if obj.is_valid():
            obj.save()
        return redirect('/view_slider')
    return render(request,"add_slider.html",{'form':obj,'sliders':slider})

def view_slider(request):
    slider = sliders.objects.all()
    return render(request,'view_slider.html',{'sliders':slider})

def delete_slide(request,del_id2):
    print("ID=",del_id2)
    sliders.objects.filter(id=del_id2).delete()
    return redirect(request,'/view_slider')

def edit_slide(request,edit_id2):

    slide= sliders.objects.filter(id=edit_id2).get()
    if request.method == 'POST' :
        form = sliderModelForm(request.POST, request.FILES ,instance=slide)
        if form.is_valid():
            form.save()
            return redirect('/view_slider')
    else:
        form =  sliderModelForm(instance=slide)
    return redirect(request,'add_slider.html',{'form':form})

# categories ============================================================


def add_categorie(request):
    categorie = categories.objects.all()
    obj = categorieModelForm()

    if 'save' in request.POST:
        obj =categorieModelForm(request.POST,request.FILES)
        if obj.is_valid():
            obj.save()
        return redirect('/view_categorie')

    return render(request,'add_categorie.html',{'form':obj,'categories':categorie})


def view_categorie(request):
    categorie = categories.objects.all()
    return render(request,'view_categorie.html',{'categories':categorie})

def delete_categorie(request,del_id3):
    print("ID=",del_id3)
    categories.objects.filter(id=del_id3).delete()
    return redirect('/view_chefs')

def edit_categorie(request,edit_id3):
    categorie = categories.objects.filter(id=edit_id3).get()
    if request.method == 'POST':        
        form = categorieModelForm(request.POST, request.FILES, instance=categorie)
        if form.is_valid():
            form.save()
            return redirect('/view_categorie')
    else:
        
        form = categorieModelForm(instance=categorie)
        
        

    return render(request,'add_categorie.html',{'form':form})

# product ===============================================================================

def shop(request):
    # categories 
    pro_cats=categories.objects.all()

    user_id = request.session.get('page_id')
    all_carts = carts.objects.filter(user_id=user_id)
    total_cart = all_carts.aggregate(total=Sum('qty'))['total'] or 0

    all_likes = likes.objects.filter(user_id=user_id)
    total_like = all_likes.aggregate(total=Sum('user_id'))['total'] or 0

    all_product = products.objects.all()   
    return render(request,'shop.html',{'total_like':total_like,'total_cart':total_cart,'cat':pro_cats,'products':all_product})


# shop page 

def add_product(request):
    product = products.objects.all()
    obj = productModelForm()

    if 'save' in request.POST:
        obj =productModelForm(request.POST,request.FILES)
        if obj.is_valid():
            obj.save()
        return redirect('/view_product')
    return render(request,'add_product.html',{'form':obj,'products':product})

def view_product(request):
    product = products.objects.all()
    return render(request,'view_product.html',{'products':product})

def delete_product(request,del_id4):
    print("ID=",del_id4)
    products.objects.filter(id=del_id4).delete()
    return redirect('/view_product')

def edit_product(request,edit_id4):
    product = products.objects.filter(id=edit_id4).get()
    if request.method == 'POST':        
        form = productModelForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/view_product')
    else:
            
        form = productModelForm(instance=product)
        
        

    return render(request,'add_product.html',{'form':form}) 

def add_cart_func(request,prod_id):
    product = products.objects.get(id=prod_id)
    u_id = request.session['page_id']
    checkExist = carts.objects.filter(product_id=prod_id,user_id=u_id)
    if checkExist.count()==0:    
        obj = carts(
            product_id = product,
            price = product.price,
            qty = 1,
            user_id = request.session['page_id']
        )
        obj.save()
    else:
        existRow = checkExist.get()
        existRow.qty = int(existRow.qty)+1
        existRow.save()
    return redirect('/cart');

def cart(request):
     # categories 
    pro_cats=categories.objects.all()

    if request.method == "POST":
        qty = request.POST['qty']
        cart_id = request.POST['cart_id']
        #product_id = request.POST['product_id']
        obj = carts.objects.filter(id=cart_id).get()
        obj.qty = qty
        obj.save()
   
    # product count..
    user_id = request.session.get('page_id')
    all_carts = carts.objects.filter(user_id=user_id)
    total_cart = all_carts.aggregate(total=Sum('qty'))['total'] or 0

    all_likes = likes.objects.filter(user_id=user_id)
    total_like = all_likes.aggregate(total=Sum('user_id'))['total'] or 0

    
    return render(request,'cart.html',{'total_like':total_like,'cat':pro_cats,'carts':all_carts,'total_cart': total_cart})

def delete_cart(request,del_id5):
    print("ID=",del_id5)
    carts.objects.filter(id=del_id5).delete()
    return redirect('/cart')

def edit_cart(request,edit_id5):
    
    cart = carts.objects.filter(id=edit_id5).get()
    if request.method == 'POST':        
        form = cartModelForm(request.POST, request.FILES, instance=cart)
        if form.is_valid():
            form.save()
            return redirect('/view_cart')
    else:
        
        form= cartModelForm(instance=cart)
    return render(request,'add_cart.html',{'form':form}) 

def add_like(request,prod_id):
    product = products.objects.get(id=prod_id)
    obj = likes(
        product_id = product,
        price = product.price,
        user_id = request.session['page_id']
    )
    obj.save()
    return redirect('/like');

def like(request):
     # categories 
    pro_cats=categories.objects.all()

    if request.method == "POST":
        like_id = request.POST['like_id']
        product_id = request.POST.get['product_id']
        obj = likes.objects.filter(id=like_id).get()
       
        obj.save()
   
    # product count..
    user_id = request.session.get('page_id')
    all_carts = carts.objects.filter(user_id=user_id)
    total_cart = all_carts.aggregate(total=Sum('qty'))['total'] or 0
    
    all_likes = likes.objects.filter(user_id=user_id)
    total_like = all_likes.aggregate(total=Sum('user_id'))['total'] or 0
   

    return render(request,'like.html',{'cat':pro_cats,'carts':all_carts,'total_cart': total_cart,'likes':all_likes,'total_like':total_like})

def delete_like(request,del_id7):
    print("ID=",del_id7)
    likes.objects.filter(id=del_id7).delete()
    return redirect('/like')
def checkout(request):
    return render(request,'checkout.html')

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

def contactpage(request):
    

    if 'save' in request.POST:
        Name=request.POST['name']
        Email=request.POST['email']
        Subject=request.POST['subject']
        Msg=request.POST['msg']
        Password=request.POST['password']
        
        obj = contact(
            name=Name,
            email=Email,
            subject=Subject,
            msg=Msg,
            password=Password,
        )
        obj.save()

        return redirect('/view_contact')
    return render(request,'contact.html')

def view_contact(request):
    data = contact.objects.all()
    return render(request,'view_contact.html',{'rows':data})

def product_detail(request,product_id):
     # categories 
    pro_cats=categories.objects.all()

    product = products.objects.filter(id=product_id).get()
    all_product = products.objects.all()
    
    # all_reviews = review.objects.filter(user_id=user_id)
    
    # cart
    cart = carts.objects.all()
    user_id = request.session.get('page_id')

    all_carts = carts.objects.filter(user_id=user_id)
    total_cart = all_carts.aggregate(total=Sum('qty'))['total'] or 0
    #like
    all_likes = likes.objects.filter(user_id=user_id)
    total_like = all_likes.aggregate(total=Sum('user_id'))['total'] or 0

    # review
    reviews = review.objects.filter(product=product_id,user_id=user_id)
    total_review = review.objects.filter(product=product_id).count()
    msg = ""
    
    if 'save' in request.POST:
        Name = request.POST['fullname']
        Email = request.POST['email']
        comments = request.POST['comment']
        Rating = request.POST['rating']
    
        obj = review(
            fullname=Name,
            email=Email,
            comment=comments,
            rating=Rating,
            product=product,
            user_id = request.session['page_id']
        )
        obj.save()
        return redirect('/view_comment')
   
    return render(request,'product_detail.html',{'total_like':total_like,'total_review': total_review,'cart':cart,'msg':msg,'reviews':reviews,'total_cart':total_cart,'cat':pro_cats,'products':all_product,'product':product})

def view_comment(request):
    data = review.objects.all()
    return render(request,'view_comment.html',{'rows':data})
    
def delete_review(request,del_id6):
    print("ID=",del_id6)  
    review.objects.filter(id=del_id6).delete()
    return redirect('/view_comment')

def catagory(request,cat_id):
    pro_cats=categories.objects.all()

    catagory = categories.objects.filter(id=cat_id).get()
    catagory_products = products.objects.filter(cat_id=catagory)
   
    user_id = request.session.get('page_id')
    all_carts = carts.objects.filter(user_id=user_id)
    total_cart = all_carts.aggregate(total=Sum('qty'))['total'] or 0
    
    all_likes = likes.objects.filter(user_id=user_id)
    total_like = all_likes.aggregate(total=Sum('user_id'))['total'] or 0

    return render(request,'category.html', {'total_like':total_like,'total_cart':total_cart,'cat': pro_cats, 'catagory_products': catagory_products, 'catagory': catagory})

def logout(request):
    if 'page_id' in request.session:
        del request.session['page_id']

    user_id = request.session.get('page_id')
    carts.objects.filter(user_id=user_id).delete()
    likes.objects.filter(user_id=user_id).delete()
    
    return redirect('/')