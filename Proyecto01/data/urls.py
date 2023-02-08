from django.urls import path
from data.views import create_index_view, update_index_view, crud_index_views, IndexDeleteView

urlpatterns = [
    path('create-index/', create_index_view),
    path('update-index/<int:pk>/', update_index_view),
    path('delete-index/<int:pk>/', IndexDeleteView.as_view(),),
    path('crud-index/', crud_index_views, name='crud_index_view'),
]