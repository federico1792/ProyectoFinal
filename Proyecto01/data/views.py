from django.shortcuts import render
from data.models import IndexChange
from data.forms import IndexChangeForm
from django.views.generic import DeleteView
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def create_index_view(request):
    if request.method == 'GET':
        context = {
            'form': IndexChangeForm(),
        }
        return render(request, 'data/create_view.html', context=context)
    elif request.method == 'POST':
        form = IndexChangeForm(request.POST, request.FILES)
        if form.is_valid():
            IndexChange.objects.create(
                    cond = form.cleaned_data['cond'],
                    background = form.cleaned_data['background'],
                    team = form.cleaned_data['team'],
                    img1 = form.cleaned_data['img1'],
                    title1 = form.cleaned_data['title1'],
                    description1 = form.cleaned_data['description1'],
                    img2 = form.cleaned_data['img2'],
                    title2 = form.cleaned_data['title2'],
                    description2 = form.cleaned_data['description2'],
                    img3 = form.cleaned_data['img3'],
                    title3 = form.cleaned_data['title3'],
                    description3 = form.cleaned_data['description3'],
            )
            context = {
                'message': 'Vista creada exitosamente'
            }
            return render(request, 'data/create_view.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': IndexChangeForm()
            }
            return render(request, 'data/create_view.html', context=context)
@staff_member_required
def update_index_view(request, pk):
    view = IndexChange.objects.get(id=pk)
    data = {
        'form': IndexChangeForm(instance=view)
    }

    if request.method == 'POST':
        formulario = IndexChangeForm(data=request.POST, instance=view, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            context = {
                'message': 'Vista modificada exitosamente'
            }
            return render(request, 'data/update_view.html', context=context)
        data['form'] = formulario
    return render(request, 'data/update_view.html', data)
@staff_member_required
def crud_index_views(request):
    if 'search' in request.GET:
        search = request.GET['search']
        data = IndexChange.objects.filter(title__icontains=search)
    else:
        data = IndexChange.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'data/crud_view.html', context=context)

class IndexDeleteView(DeleteView):
    model = IndexChange
    template_name = 'data/delete_view.html'
    success_url = '/data/crud-index/'
