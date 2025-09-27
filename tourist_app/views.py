
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .serializers import TourSerializer
from .models import Tour
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib import messages
import requests
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from .forms import TourForm

#


class TourCreateView(generics.ListCreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [AllowAny]

class TourDetail(generics.RetrieveAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

class TourUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

class TourDelete(generics.DestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer


class TourSearchViewSet(generics.ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

    def get_queryset(self):
        name = self.kwargs.get('Name')
        return Tour.objects.filter(Name__icontains=name)

def create_tour(request):
    if request.method == 'POST':
        form = TourForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                api_url='http://127.0.0.1:8000/create/'
                files = {'Tour_img': request.FILES['Tour_img']}
                data = form.cleaned_data
                response = requests.post(api_url, data=data, files=files)
                if response.status_code == 201:
                    messages.success(request, 'Tour Created Successfully')
                else:
                    messages.error(request, f'Error during API request {response.status_code}')
                return redirect('/')
            except requests.RequestException as e:
                messages.error(request, f'Error during API request {str(e)}')
        else:
            messages.error(request, 'Form is not valid')
    else:
        form = TourForm()
    return render(request, 'create_tour.html', {'form': form})


def update_tour(request, id):
    tour = Tour.objects.get(id=id)
    if request.method == 'POST':
        form = TourForm(request.POST, request.FILES, instance=tour)
        if form.is_valid():
            try:
                form.save()
                api_url=f'http://127.0.0.1:8000/update/{id}/'
                data = form.cleaned_data
                response = requests.put(api_url, data=data, files={'Tour_img': request.FILES.get('Tour_img')})
                if response.status_code == 200:
                    messages.success(request, 'Tour updated Successfully')
                else:
                    messages.error(request, f'Error during API request {response.status_code}')
                return redirect('/')
            except requests.RequestException as e:
                messages.error(request, f'Error during API request {str(e)}')
        else:
            messages.error(request, 'Form is not valid')
    else:
        form = TourForm(instance=tour)
    return render(request, 'update_tour.html', {'form': form, 'tour': tour})




def tour_delete(request, id):
    if request.method == 'POST':
        tour = Tour.objects.get(id=id)
        tour.delete()
        messages.success(request, 'Tour deleted successfully!')
        return redirect('index')
    else:
        tour = Tour.objects.get(id=id)
        return render(request, 'delete.html', {'tour': tour})





def index(request):
    if request.method == 'POST':
        search = request.POST['search']
        api_url = f' http://127.0.0.1:8000/search/{search}/'
        try:
            response = requests.get(api_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            return render(request, 'index.html', {'error_message': f'Error: {err}'})
        data = response.json()
        return render(request, 'index.html', {'tours': data})
    else:
        api_url = 'http://127.0.0.1:8000/create/'
        try:
            response = requests.get(api_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            return render(request, 'index.html', {'error_message': f'Error: {err}'})
        data = response.json()
        paginator = Paginator(data, 6)
        page = request.GET.get('page', 1)
        try:
            tours = paginator.page(page)
        except PageNotAnInteger:
            tours = paginator.page(1)
        except (EmptyPage, InvalidPage):
            tours = paginator.page(paginator.num_pages)
        return render(request, 'index.html', {'tours': tours})


def tour_fetch(request, id):
    api_url = f'http://127.0.0.1:8000/details/{id}'
    try:
        response = requests.get(api_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        return render(request, 'tour_fetch.html', {'error_message': f'Error: {err}'})

    data = response.json()

    if 'Description' in data:
        features = [f.strip() for f in data['Description'].split('.')]
    else:
        features = []

    if 'Location' in data:
        locations = data['Location'].split(',')
        if len(locations) > 1:
            state = locations[0].strip()
            district = locations[1].strip()
        else:
            state = locations[0].strip()
            district = ''
    else:
        state = ''
        district = ''

    return render(request, 'tour_fetch.html', {
        'tour': data,
        'features': features,
        'state': state,
        'district': district
    })


























