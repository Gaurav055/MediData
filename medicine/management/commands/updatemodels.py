from django.core.management.base import BaseCommand
import pandas as pd
from medicine.models import Medicine
class Command(BaseCommand):
    help = 'import file'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        #DB Connections Here
        df=pd.read_csv('meddata.csv')
        for Sku_num,Product_num,Sku_name,Price,Manufacturer_name,Salt_name,Drug_form,Pack_Size,Strength,Product_banned_flag,Unit,Price_per_unit in zip(df.sku_id,df.product_id,df.sku_name,df.price,df.manufacturer_name,df.salt_name,df.drug_form,df.Pack_size,df.strength,df.product_banned_flag,df.unit,df.price_per_unit):
            models=Medicine(sku_num=Sku_num,product_num=Product_num,sku_name=Sku_name,price=Price,manufacturer_name=Manufacturer_name,salt_name=Salt_name,drug_form=Drug_form,Pack_size=Pack_Size,strength=Strength,product_banned_flag=Product_banned_flag,unit=Unit,price_per_unit=Price_per_unit)
            models.save()


