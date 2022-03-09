from django.shortcuts import render
from .forms import PhotoForm
from django.http import HttpResponse, JsonResponse
# Create your views here.

def photo_add_view(request):
    form = PhotoForm(request.POST or None, request.FILES or None)
    data = {}
    if form.is_valid():
        form.save()
        data['name'] = form.cleaned_data.get('name')
        data['status'] = 'ok'
        return JsonResponse(data)
      
    context = {
        'form': form,
    }
    return render(request, 'photo.html', context)