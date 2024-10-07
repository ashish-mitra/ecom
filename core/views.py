from django.shortcuts import render , get_object_or_404, redirect
from .models import Painting, Category, Cart, CartItem, Order, OrderItem
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def profile(request):
    return render(request, 'user dashboard.html', {'user': request.user})

def category(request, cat):
    
    try:
        category = Category.objects.get(name=cat)
        painting = Painting.objects.filter(category=category )
   
        return render(request, "category.html", {'painting':painting, 'category':category})
    except:
        return redirect('home')


def search_paintings(request):
    query = request.GET.get('q', '') 
    if query:
        
        results = Painting.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    else:
        results = Painting.objects.all()  

    
    return render(request, 'searches.html', {'results': results, 'query': query})

def home(request):
    # messages.success(request, "welcome to home")
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username= username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "user dashboard.html" , {'user':user})
        else:
            return redirect('login')
    else:
        return render(request, "login.html")


    

def logout_user(request):
    logout(request)
    return redirect('home')

def signup_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                
               
                login(request, user)
                
                messages.success(request, "Account created successfully!")
                return redirect('home')
            else:
                messages.error(request, "Username already taken.")
        else:
            messages.error(request, "Passwords do not match.")
    
    return render(request, 'signup.html')


def base(request):
    return render(request, "based.html")

def product(request, pk):
    painting = Painting.objects.get(id = pk)

    return render(request, "product.html", {'painting': painting})

@login_required
def add_to_cart(request, painting_id):
    painting = get_object_or_404(Painting, id=painting_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, painting=painting)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view_cart')



@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('view_cart')

@login_required
def view_cart(request):
    
    cart, created = Cart.objects.get_or_create( user=request.user)
    

    cart_items = cart.cartitem_set.all()  
    total_price = sum(item.painting.price * item.quantity for item in cart_items)
    
    
    return render(request, 'cart.html', {
        'cart': cart,
        'cart_items': cart_items,
        'total_price': total_price
    })


def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.cartitem_set.all()

    if request.method == 'POST':
        
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zip_code = request.POST['zip']


        order = Order.objects.create(
            user=request.user,
            shipping_address=address,
            shipping_city=city,
            shipping_state=state,
            shipping_zip=zip_code
        )

        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                painting=cart_item.painting,
                quantity=cart_item.quantity
            )

        # Clear the cart after placing the order
        cart.cartitem_set.all().delete()


        return redirect('order_confirmation', order_id=order.id)

    return render(request, 'checkout.html', {'cart_items': cart_items})


@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = order.orderitem_set.all()
    
    return render(request, 'order_confirmation.html', {'order': order, 'order_items': order_items})

@login_required
def view_orders(request):
    
    orders = Order.objects.filter(user=request.user).order_by('-date_ordered')
    
    return render(request, 'orders.html', {'orders': orders})


@login_required
def direct_order(request, painting_id):
    painting = get_object_or_404(Painting, id=painting_id)

    if request.method == 'POST':
        

        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zip_code = request.POST['zip']


        order = Order.objects.create(
            user=request.user,
            shipping_address=address,
            shipping_city=city,
            shipping_state=state,
            shipping_zip=zip_code
        )


        order_item = OrderItem.objects.create(order=order, painting=painting, quantity=1)
        

        order.complete = True
        # order.total_price = order_item.get_total()
        order.save()


        return redirect('order_confirmation', order_id=order.id)

    return render(request, 'direct_order.html', {'painting': painting})