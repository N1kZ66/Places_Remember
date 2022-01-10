from django.urls import path
from mainapp import views


urlpatterns = [
    path('', views.BasePlaceView.as_view(), name='base'),
    path('home/', views.ListPlaceView.as_view(), name="home"),
    path("create/", views.CreatePlaceView.as_view(), name="create"),
    path("mainapp/<slug:pk>/", views.UpdatePlaceView.as_view(), name="update"),
    path("mainapp/<slug:pk>/delete/", views.DeletePlaceView.as_view(), name="delete"),
]
