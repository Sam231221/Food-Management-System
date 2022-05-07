from django.shortcuts import render
from .forms import PhotoForm
from .models import Photo
from django.views.generic import TemplateView, View
from django.http import HttpResponse, JsonResponse
import json


class PhotoListView(TemplateView):
  template_name = "photo/ajaxlive_listing.html"
  def get_context_data(self, **kwargs):
     
    context = super().get_context_data(**kwargs)
    context["photos"] =Photo.objects.all()
    return context
       
class PhotoJsonView(View):
   def get(self , request):
       print(list(Photo.objects.values()))
       return JsonResponse(list(Photo.objects.values()), safe=False)

def photo_add_view(request):
    form = PhotoForm()
    if request.method == "POST":
        data=json.loads(request.body)
        image, name, description =data['image'], data['name'], data['description']
        print(image)
        if image and name and description:
            Photo.objects.create(name=name, image=image, description =description)
            return JsonResponse({"status": 200}, safe=False)
                
    context = {
        'form': form,
    }
    return render(request, 'photo/photo1.html', context)


       
def upload_progress_image(request):
    form = PhotoForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = PhotoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
                form.save()
                return JsonResponse({'message': 'hell yeah'})
        else:
            return HttpResponse('Invalid')   

    return render(request, 'photo/photo2.html', context)
    
def staging_image(request):
    return JsonResponse('Image in Staging area',safe=False)