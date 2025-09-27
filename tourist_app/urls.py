from django.urls import path
from . import views

urlpatterns = [
    # Tour CRUD Operations
    path('create_tour/', views.create_tour, name='create_tour'),
    path('update_tour/<int:id>/', views.update_tour, name='update_tour'),
    path('tour_fetch/<int:id>/', views.tour_fetch, name='tour_fetch'),

    path('delete/<int:id>/', views.tour_delete, name='tour_delete'),



    # API Views
    path('create/', views.TourCreateView.as_view(), name='tour_list'),
    path('details/<int:pk>/', views.TourDetail.as_view(), name='tour_detail'),
    path('update/<int:pk>/', views.TourUpdateView.as_view(), name='tour_update'),
    path('delete/<int:pk>/', views.TourDelete.as_view(), name='tour_delete'),
    path('search/<str:Name>/', views.TourSearchViewSet.as_view(), name='tour_search'),
    path('', views.index, name='index'),
]
