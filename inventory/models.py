from django.db import models

class Warehouse(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    location = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, default=1)
    cost_per_item  = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    Quantity_in_stock = models.IntegerField(null=False, blank=False)
    Quantity_sold =  models.IntegerField(null=False, blank=False)
    sales = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    stock_date = models.DateField(auto_now_add=True)
    last_sales_date =  models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.
