from django.shortcuts import get_object_or_404, redirect, render
from multimodelsapp.forms import CustomerForm

from multimodelsapp.models import Customer, Product ,Order

# Create your views here.

def customer_list(request):
    customers = Customer.objects.all()
    # products = Product.objects.all()
    # orders = Order.objects.all()
    # context = {'customers':customers,'products':products,'orders':orders}
    return render(request,'multimodelsapp/customer_list.html',{'customers':customers,})

def customer_create(request):
    form = CustomerForm()
    if request.method =='POST':
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers_lists')
    return render(request,'multimodelsapp/customer_create.html',{'form':form})




def customer_update(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers_lists')
    else:
        form = CustomerForm(instance=customer)

    return render(request, 'multimodelsapp/customer_update.html', {'form': form})



def customer_delete(request,id):
    customer =Customer.objects.get(id=id)
    customer.delete()
    return redirect('customers_lists')































