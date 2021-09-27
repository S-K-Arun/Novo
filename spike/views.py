from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from .models import Movie, upload,Art,Buildings,Cars,Academi

def images(request):
    Movies = Movie.objects.all()
    context = {'Movies' : Movies }
    return render(request,'spike/main.html',context)

def academi(request):
    ACedemi = Academi.objects.all()
    context = {'ACedemi' : ACedemi }
    return render(request,'spike/academic.html',context)

def art(request):
    ARt = Art.objects.all()
    context = {'ARt' : ARt }
    return render(request,'spike/art.html',context)

def buildings(request):
    BUildings = Buildings.objects.all()
    context = {'BUildings' : BUildings }
    return render(request,'spike/building.html',context)

def cars(request):
    CAr = Cars.objects.all()
    context = {'CAr' : CAr }
    return render(request,'spike/cars.html',context)

class Mainview(TemplateView):
    template_name = "spike/main2.html"

def file_upload_view(request):
    if request.method == 'POST':
        my_file = request.FILES.get('file')
        upload.objects.create(upload=my_file)
        return HttpResponse('')
    return JsonResponse({'post':'false'})

