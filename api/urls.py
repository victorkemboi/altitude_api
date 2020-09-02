from django.urls import path,include
from rest_framework import routers

from api import views

urlpatterns = [
    path('register', views.RegistrationView.as_view(),name='Register'),
    path('login', views.ObtainAuthToken.as_view(),name='Login'),
    path('categories', views.CategoriesView.as_view(),name='Categories'),
    path('sub_categories', views.SubCategoriesView.as_view(),name='SubCategories'),
    path('airlines', views.AirlinesView.as_view(),name='Airlines'),
    path('magazines', views.MagazinesView.as_view(),name='Magazines'),


]