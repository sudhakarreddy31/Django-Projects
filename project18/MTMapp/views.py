from django.shortcuts import get_object_or_404, redirect, render

from MTMapp.models import Product
from MTMapp.forms import ProductForm

# Create your views here.

def products_list(request):
    products = Product.objects.all()
    return render(request,'MTMapp/products_lists.html',{'products':products})


def product_create(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_lists')
        
    return render(request,'MTMapp/products_create.html',{'form':form})


def product_update(request,id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_lists')
    else:
        form = ProductForm(instance=product)
        cat = product.categories.all()


    return render(request,'/home/sudhakarreddy/Django-Projects/project18/MTMapp/templates/products_update.html',{'form':form,'cat':cat,'product':product})




def product_delete(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('product_lists')
