from django.db import models
from .category import CATEGORY




# Define Product model
class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name
    
class staff(models.Model):
    staff_name=models.CharField(max_length=100,null=True)
    staff_number=models.PositiveIntegerField(null=True)
    staff_email=models.EmailField(max_length=100,null=True)

    def __str__(self):
        return self.staff_name or 'Unnamed Staff'




class buyer(models.Model):
    buyer_name=models.CharField(max_length=100,null=True)
    buyer_number=models.IntegerField()
    buyer_address=models.TextField(null=True)
    buyer_email=models.EmailField(max_length=100)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    buyer_pincode=models.IntegerField()
    product_quantity=models.IntegerField()
    # Seller=models.ForeignKey(Seller,on_delete=models.CASCADE)

    def __str__(self) :
        return self.buyer_name
    
class Seller(models.Model):
    seller_name=models.CharField(max_length=100,null=True)
    seller_email=models.EmailField(max_length=100)
    seller_address=models.TextField()
    seller_number=models.IntegerField()
    seller_quantity=models.IntegerField()
   
    Buyer=models.ForeignKey(buyer,on_delete=models.CASCADE)
  
    

    def __str__(self) :
        return self.seller_name

