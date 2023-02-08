from django.urls import path
from sales.views import list_sales, update_sale, detail_sale, crud_sales, create_sale, SaleDeleteView

urlpatterns = [
    path('list-sale/', list_sales),
    path('detail-sale/<int:pk>', detail_sale),
    path('create-sale/', create_sale),
    path('update-sale/<int:pk>/', update_sale),
    path('delete-sale/<int:pk>/', SaleDeleteView.as_view(),),
    path('crud-sale/', crud_sales, name='crud_sale'),
]