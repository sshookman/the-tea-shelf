from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Tea

def index(request):
    teas = Tea.objects.order_by('-name')
    return render(request, 'shelf/index.html', {'teas':teas})

def form(request):
    return render(request, 'shelf/form.html')

def add(request):
    print(request.POST['name'])
    return HttpResponseRedirect(reverse('form'))

def detail(request, tea_id):
    tea = get_object_or_404(Tea, pk=tea_id)
    return render(request, 'shelf/details.html', {'tea':tea})

def timer(request, tea_id):
    tea = get_object_or_404(Tea, pk=tea_id)
    return render(request, 'shelf/timer.html', {'tea':tea})
