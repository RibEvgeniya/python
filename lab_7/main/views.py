from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Client
# Create your views here.


def client_home(request):
    return HttpResponse('<h1>Client home</h1>')

def client_detail(request,id):
    instance=get_object_or_404(Client,id=id)
    context=\
        {
            'instance': instance,
            'title': 'Детали о клиенте',
        }
    return render(request, 'client_detail.html', context)
def client_list(request):
    queryset=Client.objects.all()
    context = {
        'queryset': queryset,
        'title': 'Список всех клиентов',
        'name':'Клиенты'
    }
    return render(request,'form.html',context)