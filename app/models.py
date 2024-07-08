from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    CategoryName=models.CharField(max_length=100,primary_key=True)
    CategoryId=models.IntegerField()

    def __str__(self):
        return self.CategoryName
    
class Product(models.Model):
    CategoryName=models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    ProductName=models.CharField(max_length=100)
    ProductId=models.IntegerField(primary_key=True)
    ProductPrice=models.IntegerField()
    ProductDate=models.DateField()

    def __str__(self):
        return self.ProductName