from django.db import models

# Create your models here.
class Medicine(models.Model):
    # sku_num=models.IntegerField(null=True)
    sku_num=models.TextField(null=True)
    # product_num=models.IntegerField(null=True)
    product_num=models.TextField(null=True)
    sku_name=models.CharField(max_length=255)
    # price=models.DecimalField(max_digits=6,decimal_places=2)
    price=models.TextField()
    manufacturer_name=models.TextField()	
    salt_name=models.TextField()	
    drug_form=models.CharField(max_length=255)	
    Pack_size=models.CharField(null=True,max_length=255)	
    strength=models.TextField(null=True)	
    product_banned_flag=models.TextField(null=True)	
    unit=models.TextField(null=True)	
    price_per_unit=models.TextField(null=True)

    def __str__(self):
        return self.sku_name