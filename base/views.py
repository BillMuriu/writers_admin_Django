from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm

# Create your views here.

def home(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'base/home.html', context)

def room(request):
    return render(request, 'room.html')

def createOrder(request):
    form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/order_form.html', context)
