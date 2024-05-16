from django.urls import path
from django.conf import settings
from . import views
# from django.conf.urls.static import static

urlpatterns = [
    # path("", views.index, name="index"),
    path('', views.dashboard, name='dashboard'),
    path('prediksi/', views.prediksi, name='prediksi'),
    path('customer_journey_mapping/', views.customerjourneymap, name='customer_journey_mapping'),
    path('customer_journey_mapping/graph/', views.customerjourneymap_graph, name='customer_journey_mapping_graph'),
    path('analisa/', views.analisa, name='analisa'),
]