from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Client
from .forms import ClientForm
# Create your views here.


def client_create(request):
    form=ClientForm()
    if request.method=='POST':
        name=request.POST.get('name')
        surname = request.POST.get('surname')
        patronymic = request.POST.get('patronymic')
        phone=request.POST.get('phone')
        Client.objects.create(name=name,surname=surname,patronymic=patronymic,phone=phone)
    context={
    'form':form,
    }
    return render(request, 'add_client.html', context)


def client_update(request,id1):
    instance = get_object_or_404(Client, id=id1)
    form=ClientForm(request.POST,instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        form.cleaned_data.get('name')
    context={
        'form':form,
        'instance':instance,
        'id':id1,
    }
    return render(request, 'update_client.html', context)

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