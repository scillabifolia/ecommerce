from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product

# Create your views here.

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/product_list.html"

    # def get_context_data(self,*args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/product_list.html", context)



class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self,*args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        #context['abc'] =123
        return context


def product_detail_view(request, pk=None, *args, **kwargs):
    #  pk(primary_key) is also the id which will increment authomaticly
    #instance = Product.objects.get(pk=pk)

    #instance = get_object_or_404(Product, pk=pk)
    # try:
    #     instance = Product.objects.get(id=pk)
    #
    # # except Product.DoesNotExist:
    # #     print('no product here')
    # #     raise Http404("Product doesn't exist")
    # # except Product.DoesNotExist:
    # #     print('huh?')

    instance = Product.objects.get(id=pk)
    if instance is None:
        raise Http404("Product doesn't exist")
    # print(instance)
    #
    # qs = Product.objects.filter(id=pk)

    # # print(qs)
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404("Product doesn't exist")

    context = {
        'object_list': instance,
        'abc': 123
    }
    return render(request, "products/detail.html", context)


