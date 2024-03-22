from django.db import models
from django.forms import ModelForm
from django import forms
# Create your models here.

class sliders(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    image = models.FileField(upload_to='./media/')

class sliderModelForm(ModelForm):
    class Meta:
        model = sliders
        fields = ["title","desc","image"]


    
class categories(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='./media/')

    def __str__(self):
        return self.title 
    
class categorieModelForm(ModelForm):
    class Meta:
        model = categories
        fields = ["title","image"]
        
class products(models.Model):
    cat_id=models.ForeignKey(categories,on_delete=models.CASCADE, default=0)
    name=models.CharField(max_length=1000)
    price=models.CharField(max_length=1000)
    desc = models.CharField(max_length=1000)
    image = models.FileField(upload_to='./media/')

    
class productModelForm(ModelForm):
    class Meta:
        model=products
        fields=["cat_id","name","price","desc","image"]

    
class carts(models.Model):
    product_id=models.ForeignKey(products,on_delete=models.CASCADE, default=0)
    price = models.CharField(max_length=1000)
    qty = models.CharField(max_length=1000)
    user_id= models.IntegerField(default=0)
    def total_cost(self):
        return int(self.qty) * int(self.price)
    
  

class cartModelForm(ModelForm):
    class Meta:
        model=carts
        fields=["product_id","price","qty","user_id"]

class likes(models.Model):
    product_id=models.ForeignKey(products,on_delete=models.CASCADE, default=0)
    price = models.CharField(max_length=1000)
    user_id= models.IntegerField(default=0)

class likeModelForm(ModelForm):
    class Meta:
        model=likes
        fields=["product_id","price","user_id"]   

class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    msg = models.CharField(max_length=300)
    password = models.CharField(max_length=100)

class review(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    comment = models.CharField(max_length=300)
    product = models.ForeignKey(products,default=13,on_delete=models.CASCADE)
    rating = models.IntegerField()
    user_id= models.IntegerField(default=0)

    