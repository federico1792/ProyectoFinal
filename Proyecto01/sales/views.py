from django.shortcuts import render
from sales.models import Sale
from sales.forms import SaleForm
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def create_sale(request):
    if request.method == 'GET':
        context = {
            'form': SaleForm(),
        }
        return render(request, 'sales/create_sale.html', context=context)
    elif request.method == 'POST':
        form = SaleForm(request.POST, request.FILES)
        if form.is_valid():
            Sale.objects.create(
                    title = form.cleaned_data['title'],
                    zone = form.cleaned_data['zone'],
                    description = form.cleaned_data['description'],
                    price = form.cleaned_data['price'],
                    environments = form.cleaned_data['environments'],
                    toilets = form.cleaned_data['toilets'],
                    area = form.cleaned_data['area'],
                    sold = form.cleaned_data['sold'],
                    sale_image = form.cleaned_data['sale_image'],
            )
            context = {
                'message': 'Propiedad creada exitosamente'
            }
            return render(request, 'sales/create_sale.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': SaleForm()
            }
            return render(request, 'sales/create_sale.html', context=context)

@login_required
def detail_sale(request, pk):
    sale = Sale.objects.get(id = pk)
    if request.method == 'GET':
        context = {
            'title': sale.title,
            'zone': sale.zone,
            'description': sale.description,
            'price': sale.price,
            'environments': sale.environments,
            'toilets': sale.toilets,
            'area': sale.area,
            'sale_image': sale.sale_image,

        }
        return render(request, 'sales/detail_sale.html', context=context)
@staff_member_required
def update_sale(request, pk):
    sale = Sale.objects.get(id=pk)
    data = {
        'form': SaleForm(instance=sale)
    }

    if request.method == 'POST':
        formulario = SaleForm(data=request.POST, instance=sale, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            context = {
                'message': 'Propiedad modificada exitosamente'
            }
            return render(request, 'sales/update_sale.html', context=context)
        data['form'] = formulario
    return render(request, 'sales/update_sale.html', data)

def list_sales(request):
    if 'search' in request.GET:
        search = request.GET['search']
        sales = Sale.objects.filter(zone__icontains=search).order_by('zone')
    else:
        sales = Sale.objects.all()
    context = {
        'sales': sales,
    }
    return render(request, 'sales/list_sale.html', context=context)
@staff_member_required
def crud_sales(request):
    if 'search' in request.GET:
        search = request.GET['search']
        sales = Sale.objects.filter(title__icontains=search)
    else:
        sales = Sale.objects.all()
    context = {
        'sales': sales,
    }
    return render(request, 'sales/crud_sale.html', context=context)

class SaleDeleteView(DeleteView):
    model = Sale
    template_name = 'sales/delete_sale.html'
    success_url = '/sales/crud-sale/'

