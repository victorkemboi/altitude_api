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
    path('issues', views.IssueView.as_view(),name='Issues'),
    path('favourites', views.FavouriteMagazinesView.as_view(), name='Favourites'),
    path('subscriptions', views.SubscriptionView.as_view(), name='Subscriptions'),
    path('issue_progress', views.IssueProgressView.as_view(), name='IssueProgress'),

]