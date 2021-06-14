from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.http import HttpResponse
from .models import Category, Criteria, Subcriteria, House, HousePoints
from .forms import SubCriteriaForm

# Create your views here.


class HomeView(TemplateView):
    template_name = 'rate/home.html'

    def get_context_data(self, **kwargs):
        """
        Adds the form and enables the footer.
        """
        context = super(HomeView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            house, created = House.objects.get_or_create(
                user=self.request.user)
            context['points'] = house.total_points()
        return context


class AboutView(TemplateView):
    template_name = 'rate/about.html'


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'rate/categories.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def get_queryset(self):
        return Category.objects.order_by('name')


class CriteriaListView(LoginRequiredMixin, ListView):
    model = Criteria
    template_name = 'rate/criteria.html'

    def get_context_data(self, **kwargs):
        context = super(CriteriaListView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def get_queryset(self):
        return Criteria.objects.filter(category_id=self.kwargs['pk']).order_by('name')


class SubcriteriaListView(LoginRequiredMixin, ListView):
    model = Subcriteria
    template_name = 'rate/subcriteria.html'

    def get_context_data(self, **kwargs):
        context = super(SubcriteriaListView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['form'] = SubCriteriaForm
        return context
