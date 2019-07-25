from django.shortcuts import render, redirect, reverse
from .models import Book, LeaderBoard, Cart, Order
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import CreateOrder
from django.db.models import F

def home(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'home.html', context)

def shop(request):
    context = {
        'title' : 'Shop',
        'books' : Book.objects.all()

    }
    return render(request, 'shop.html', context)

def search_book(request):
    try :
        query_book = request.GET.get('query_book')
    except:
        query_book = None
    if query_book != "":
        books = Book.objects.filter(title = query_book)
        context = {'query ' : query_book}
        template = 'shop.html'
    else:
        books = Book.objects.all()
    template = 'shop.html'
    context = {
        'title' : 'Search',
        'books' : books,
    }
    return render(request, template,context)

def search_order(request):
    query_order = request.GET.get('query_order')
    order = ""
    if query_order:
        order = Order.objects.filter(id = query_order)
    else:
        try:
            order = Order.objects.filter(user = request.user)
        except:
            order = ""
    context = {
        'query' : query_order,
        'order' :  order,
    }

    return render(request, 'find_my_order.html',context)

def leaderboard(request):
    query = request.GET.get('query_leaderboard')
    leaderboard = LeaderBoard.objects.filter(genre = query).order_by('position')
    context = {
        'title' : 'Leaderboard',
        'query' : query,
        'leaderboard' : leaderboard,
    }
    return render(request, 'leaderboard.html',context)

@login_required()
def cart(request):
    if request.method == 'POST':
        form = CreateOrder(request.POST, instance=request.user)
        order = Order.objects.create(user = request.user)
        cart = Cart.objects.get(user=request.user)
        for book in cart.books.all():
            order.books.add(book.id)
            Book.objects.filter(id=book.id).update(units_sold=F('units_sold')+1)
        if form.data.get('address'):
            order.address = form.data.get('address')
        order.payment = form.data.get('payment')
        order.total_cost = cart.get_price()
        order.save()
        cart.books.clear()
        cart.save()
        messages.success(request, f'The order was created successfully!')

        #messages.warning(request, 'Warning : the order was not created!')
        return render(request, 'home.html')
    else:
        try:
            cart = Cart.objects.get(user = request.user)
        except:
            cart = Cart.objects.create(user = request.user)
        form = CreateOrder(instance=request.user)
        context = {
            'cart' : cart.books.all(),
            'total_price' : cart.get_price(),
            'form' : form,
            'title' : 'Cart',
        }

        return render(request, 'cart.html', context)

@login_required()
def cart_add(request, **kwargs):
    try:
        cart = Cart.objects.get(user=request.user)
        # filter products by id
        book = Book.objects.filter(id=kwargs.get('item_id', "")).first()
        # check if the user already owns this product
        if book in cart.books.all():
            messages.info(request, 'You already have this book on your cart')
            return redirect(reverse('shop'))
        cart.books.add(book)
        cart.save()
        # show confirmation message and redirect back to the same page
        messages.success(request, "Item added successfully to the cart")
    except:
        messages.warning(request, "Error! Impossible to add the item to the cart. Try again later")
    return redirect(reverse('shop'))
