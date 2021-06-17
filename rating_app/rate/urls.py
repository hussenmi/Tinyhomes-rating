from django.urls import path
from .views import HomeView, AboutView, CategoryListView, CriteriaListView, SubcriteriaListView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='rate-home'),
    path('about/', AboutView.as_view(), name='rate-about'),
    path('categories/', CategoryListView.as_view(), name='rate-categories'),
    path('criteria/<int:pk>/', CriteriaListView.as_view(), name='rate-criteria'),
    path('subcriteria/', SubcriteriaListView.as_view(), name='rate-subcriteria'),
]
