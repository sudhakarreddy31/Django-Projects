from django.shortcuts import get_object_or_404, render
from productapp.forms import ProductForm
from django.shortcuts import render, redirect
from productapp.models import Product

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request,"productapp/product_list.html",{'products':products})

def product_detail(request,id):
    product = get_object_or_404(Product,id=id)
    return render(request,'/home/sudhakarreddy/DjangoProjects/project5/productapp/templates/productapp/product_detail.html',{'product':product})


def product_create(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")    
    return render(request,'productapp/product_create.html',{'form':form})



def product_update(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm(instance=product)
    return render(request, "productapp/product_update.html", {'product': product, 'form': form})



# def product_delete(request,id):
#     employee = Product.objects.get(id=id)
#     employee.delete()
#     return redirect(product_list)




def product_delete(request, id):
    product = get_object_or_404(Product, id=id)  # Correct the argument to 'id'
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, '/home/sudhakarreddy/DjangoProjects/project5/productapp/templates/productapp/product_delete.html', {'product': product})

