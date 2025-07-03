from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Product, Order, Bank

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('grocery_home')
    return render(request, 'store/login.html')

@login_required
def grocery_home(request):
    try:
        bank = Bank.objects.get(user=request.user)
        balance = bank.balance
    except Bank.DoesNotExist:
        balance = "Not set"  # Optional: or redirect to error page / admin setup page
    return render(request, 'store/grocery_home.html', {'balance': balance})

@login_required
def vegetables(request):
    items = Product.objects.filter(category='vegetable')
    bank = Bank.objects.get(user=request.user)
    return render(request, 'store/vegetables.html', {'items': items, 'balance': bank.balance})

@login_required
def fruits(request):
    items = Product.objects.filter(category='fruit')
    bank = Bank.objects.get(user=request.user)
    return render(request, 'store/fruits.html', {'items': items, 'balance': bank.balance})

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    quantity = int(request.POST['quantity'])
    total_price = product.price * quantity
    Order.objects.create(user=request.user, product=product, quantity=quantity, total_price=total_price)
    return redirect('cart')

@login_required
def cart(request):
    orders = Order.objects.filter(user=request.user, payment_status="Pending")
    total = sum(order.total_price for order in orders)
    bank = Bank.objects.get(user=request.user)
    return render(request, 'store/cart.html', {'orders': orders, 'total': total, 'balance': bank.balance})

@login_required
def payment(request):
    orders = Order.objects.filter(user=request.user, payment_status="Pending")
    total = sum(order.total_price for order in orders)
    bank = Bank.objects.get(user=request.user)
    if request.method == 'POST':
        if total <= bank.balance:
            bank.balance -= total
            bank.save()
            orders.update(payment_status="Paid")
            return redirect('success')
        else:
            orders.update(payment_status="Incomplete")
            return redirect('failure')
    return render(request, 'store/payment.html', {'total': total, 'balance': bank.balance})

@login_required
def success(request):
    bank = Bank.objects.get(user=request.user)
    return render(request, 'store/success.html', {'balance': bank.balance})

@login_required
def failure(request):
    bank = Bank.objects.get(user=request.user)
    return render(request, 'store/failure.html', {'balance': bank.balance})

def logout_view(request):
    logout(request)
    return redirect('login')
