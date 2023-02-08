from django.urls import path
from rentals.views import list_rentals, update_rental, detail_rental, crud_rentals, create_rental, RentalDeleteView

urlpatterns = [
    path('list-rental/', list_rentals),
    path('detail-rental/<int:pk>', detail_rental),
    path('create-rental/', create_rental),
    path('update-rental/<int:pk>/', update_rental),
    path('delete-rental/<int:pk>/', RentalDeleteView.as_view(),),
    path('crud-rental/', crud_rentals, name='crud_rental'),
]