from django.shortcuts import render
from data.models import IndexChange


def index(request):
    data = IndexChange.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'index.html', context=context)

def about(request):
    return render(request, 'about.html', context={})