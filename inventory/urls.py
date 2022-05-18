from django.urls import path
from .views import ( InventoryListView, 
                    InventoryDetailView, 
                    InventoryCreateView, 
                    InventoryUpdateView, 
                    InventoryDeleteView, 
                    WarehouseCreateView,
                    dashboard)

urlpatterns = [
    path('', InventoryListView.as_view(), name='inventory-list'),
    path('product/<int:pk>/', InventoryDetailView.as_view(), name='inventory-detail'),
    path('product/new/', InventoryCreateView.as_view(), name='inventory-new'),
    path('product/update/<int:pk>/', InventoryUpdateView.as_view(), name='inventory-update'),
    path('product/delete/<int:pk>/', InventoryDeleteView.as_view(), name='inventory-delete'),
    path('warehouse/create/', WarehouseCreateView.as_view(), name='warehouse-create'),
    path("dashboard/", dashboard, name="dashboard"),
]

