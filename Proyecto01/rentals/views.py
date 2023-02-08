from django.shortcuts import render
from rentals.models import Rental
from rentals.forms import RentalForm
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def create_rental(request):
    if request.method == 'GET':
        context = {
            'form': RentalForm(),
        }
        return render(request, 'rentals/create_rental.html', context=context)
    elif request.method == 'POST':
        form = RentalForm(request.POST, request.FILES)
        if form.is_valid():
            Rental.objects.create(
                    title = form.cleaned_data['title'],
                    zone = form.cleaned_data['zone'],
                    description = form.cleaned_data['description'],
                    price = form.cleaned_data['price'],
                    environments = form.cleaned_data['environments'],
                    toilets = form.cleaned_data['toilets'],
                    area = form.cleaned_data['area'],
                    sold = form.cleaned_data['sold'],
                    rental_image = form.cleaned_data['rental_image'],
            )
            context = {
                'message': 'Alquiler creado exitosamente'
            }
            return render(request, 'rentals/create_rental.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': RentalForm()
            }
            return render(request, 'rentals/create_rental.html', context=context)

@login_required
def detail_rental(request, pk):
    rental = Rental.objects.get(id = pk)
    if request.method == 'GET':
        context = {
            'title': rental.title,
            'zone': rental.zone,
            'description': rental.description,
            'price': rental.price,
            'environments': rental.environments,
            'toilets': rental.toilets,
            'area': rental.area,
            'rental_image': rental.rental_image,

        }
        return render(request, 'rentals/detail_rental.html', context=context)
@staff_member_required
def update_rental(request, pk):
    rental = Rental.objects.get(id=pk)
    data = {
        'form': RentalForm(instance=rental)
    }

    if request.method == 'POST':
        formulario = RentalForm(data=request.POST, instance=rental, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            context = {
                'message': 'Alquiler modificado exitosamente'
            }
            return render(request, 'rentals/update_rental.html', context=context)
        data['form'] = formulario
    return render(request, 'rentals/update_rental.html', data)

def list_rentals(request):
    if 'search' in request.GET:
        search = request.GET['search']
        rentals = Rental.objects.filter(zone__icontains=search).order_by('zone')
    else:
        rentals = Rental.objects.all()
    context = {
        'rentals': rentals,
    }
    return render(request, 'rentals/list_rental.html', context=context)
@staff_member_required
def crud_rentals(request):
    if 'search' in request.GET:
        search = request.GET['search']
        rentals = Rental.objects.filter(title__icontains=search)
    else:
        rentals = Rental.objects.all()
    context = {
        'rentals': rentals,
    }
    return render(request, 'rentals/crud_rental.html', context=context)

class RentalDeleteView(DeleteView):
    model = Rental
    template_name = 'rentals/delete_rental.html'
    success_url = '/rentals/crud-rental/'