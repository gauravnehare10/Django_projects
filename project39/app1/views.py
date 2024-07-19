from django.shortcuts import render
from app1.models import Product
from django.views.generic import DeleteView, CreateView, TemplateView, UpdateView, ListView
from django.urls import reverse, reverse_lazy
# Create your views here.

class IndexView(TemplateView):
    template_name = 'app1/index.html'

class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'   # fields = ['prodid', 'prodname'] 
    template_name = 'app1/create_product.html'
    success_url = reverse_lazy('create')
    
class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'app1/update_product.html'
    success_url = reverse_lazy('productlist')

class ProductUListView(ListView):
    model = Product
    fields = '__all__'
    template_name = 'app1/product_update_list.html'
    context_object_name = 'products'

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('dlist')
    template_name = 'app1/prod_conf.html'
    context_object_name = 'product'

class ProductDeleteListView(ListView):
    model = Product
    fields = '__all__'
    template_name = 'app1/product_delete_list.html'
    context_object_name = 'products'

class ProductListView(ListView):
    model = Product
    fields = '__all__'
    template_name = 'app1/product_list.html'
    context_object_name = 'products'