import imp
from django.shortcuts import render
from .models import Warehouse, Inventory
from django.contrib.messages.views import SuccessMessageMixin
from  django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django_pandas.io import read_frame
import json
import plotly
import plotly.express as px

# Create your views here.

class InventoryListView(ListView):
    model = Inventory
    #template_name = 'inventory/home.html'
    context_object_name = 'inventorys'

class InventoryDetailView(DetailView):
    model = Inventory

class InventoryCreateView(SuccessMessageMixin, CreateView):
    model = Inventory
    fields = ['name', 'warehouse', 'cost_per_item', 'Quantity_in_stock', 'Quantity_sold', 'sales']
    success_url = '/'
    success_message = "%(name)s was added successfully"



class InventoryDeleteView(SuccessMessageMixin, DeleteView):
    model = Inventory
    success_url = '/'
    success_message = "Item was deleted successfully"


class InventoryUpdateView(SuccessMessageMixin, UpdateView):
    model = Inventory
    fields = ['name', 'warehouse', 'cost_per_item', 'Quantity_in_stock', 'Quantity_sold', 'sales']
    success_url = '/'
    success_message = "%(name)s was updated successfully"


class WarehouseCreateView(SuccessMessageMixin, CreateView):
    model = Warehouse
    fields = ['name', 'location']
    success_url = '/'
    success_message = "%(name)s was created successfully"


def dashboard(request):
    inventories = Inventory.objects.all()
    df = read_frame(inventories)
    
    # sales graph
    print(df.columns)
    sales_graph_df = df.groupby(by="last_sales_date", as_index=False, sort=False)['sales'].sum()
    print(sales_graph_df.sales)
    print(sales_graph_df.columns)
    sales_graph = px.line(sales_graph_df, x = sales_graph_df.last_sales_date, y = sales_graph_df.sales, title="Sales Trend")
    sales_graph = json.dumps(sales_graph, cls=plotly.utils.PlotlyJSONEncoder)

    
    # best performing product
    best_performing_product_df = df.groupby(by="name").sum().sort_values(by="Quantity_sold")
    best_performing_product = px.bar(best_performing_product_df, 
                                    x = best_performing_product_df.index, 
                                    y = best_performing_product_df.Quantity_sold, 
                                    title="Best Performing Product"
                                )
    best_performing_product = json.dumps(best_performing_product, cls=plotly.utils.PlotlyJSONEncoder)

    context = {
        "sales_graph": sales_graph,
        "best_performing_product": best_performing_product
    }

    return render(request,"inventory/dashboard.html", context=context)