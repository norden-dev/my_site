from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.main_home, name='main_home', ),
    path('about/', views.main_about, name='main_about', ),

    path('contact/', views.ContactView.as_view(), name='main_contact', ),
    path("services/", views.ServiceView.as_view(), name="main_services"),


]