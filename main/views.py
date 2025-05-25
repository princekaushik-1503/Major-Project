from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import MenuItem, Table, Reservation, Review, ContactMessage, Cart, CartItem, Order, OrderItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from decimal import Decimal
from django.views.decorators.http import require_POST

def home(request):
    menu_items = MenuItem.objects.all()[:6]
    reviews = Review.objects.all().order_by('-created_at')[:3]
    return render(request, 'main/home.html', {
        'menu_items': menu_items,
        'reviews': reviews
    })

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        city = request.POST.get('city')
        message = request.POST.get('message')
        
        # Save to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            city=city,
            message=message
        )
        
        # Send email
        try:
            email_message = f"""
            New contact form submission:
            
            Name: {name}
            Email: {email}
            City: {city}
            Message: {message}
            """
            
            send_mail(
                'New Contact Form Submission',
                email_message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, f'There was an error sending your message. Please try again later. Error: {str(e)}')
        
        return redirect('contact')
    
    return render(request, 'main/contact.html')

def menu(request):
    starters = MenuItem.objects.filter(category='Starters')
    main_courses = MenuItem.objects.filter(category='Main Courses')
    desserts = MenuItem.objects.filter(category='Desserts')
    wines = MenuItem.objects.filter(category='Fine Wines')
    
    context = {
        'starters': starters,
        'main_courses': main_courses,
        'desserts': desserts,
        'wines': wines,
    }
    return render(request, 'main/menu.html', context)

@login_required
def book_table(request):
    if request.method == 'POST':
        try:
            date = request.POST.get('date')
            time = request.POST.get('time')
            guests = int(request.POST.get('guests', 2))
            table_id = request.POST.get('table')
            
            # Validate table_id is a number
            if not table_id.isdigit():
                messages.error(request, 'Please select a valid table.')
                return redirect('book_table')
            
            table = get_object_or_404(Table, id=table_id)
            
            # Check if table is available
            if not table.is_available:
                messages.error(request, 'This table is not available. Please select another table.')
                return redirect('book_table')
            
            # Create reservation
            reservation = Reservation.objects.create(
                user=request.user,
                table=table,
                date=date,
                time=time,
                guests=guests,
                status='pending'
            )
            
            messages.success(request, 'Your table has been reserved successfully! We will confirm your reservation shortly.')
            return redirect('home')
            
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            return redirect('book_table')
    
    # Get available tables
    tables = Table.objects.filter(is_available=True)
    return render(request, 'main/book_table.html', {'tables': tables})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'main/signup.html', {'form': form})

@login_required
def add_review(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        
        Review.objects.create(
            user=request.user,
            rating=rating,
            comment=comment
        )
        
        messages.success(request, 'Review added successfully!')
        return redirect('home')
    
    return render(request, 'main/add_review.html')

@login_required
def reviews(request):
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'main/reviews.html', {
        'reviews': reviews
    })

@require_POST
@login_required
def add_to_cart(request, item_id):
    try:
        menu_item = get_object_or_404(MenuItem, id=item_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        
        # Get or create cart item
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            menu_item=menu_item,
            defaults={'quantity': 1}
        )
        
        # If item already exists, increment quantity
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        
        return JsonResponse({
            'status': 'success',
            'message': f'{menu_item.name} added to cart',
            'cart_total': cart.get_total_items()
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)

@require_POST
@login_required
def update_cart(request, item_id):
    try:
        cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        quantity = int(request.POST.get('quantity', 0))
        
        if quantity <= 0:
            cart_item.delete()
            message = 'Item removed from cart'
        else:
            cart_item.quantity = quantity
            cart_item.save()
            message = 'Cart updated successfully'
        
        cart = cart_item.cart
        return JsonResponse({
            'status': 'success',
            'message': message,
            'cart_total': cart.get_total_items(),
            'subtotal': str(cart.get_subtotal()),
            'gst': str(cart.get_gst()),
            'total': str(cart.get_total())
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()
    
    context = {
        'cart': cart,
        'cart_items': cart_items
    }
    return render(request, 'main/cart.html', context)

@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    if not cart.items.exists():
        return redirect('cart')

    if request.method == 'POST':
        # Create Order
        subtotal = cart.get_subtotal()
        gst = cart.get_gst()
        total = cart.get_total()
        order = Order.objects.create(
            user=request.user,
            subtotal=subtotal,
            gst_amount=gst,
            total_amount=total,
            payment_status=True,  # Assume payment is done after QR
            status='confirmed'
        )
        # Create OrderItems
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                menu_item=item.menu_item,
                quantity=item.quantity,
                price=item.menu_item.price
            )
        # Clear cart
        cart.items.all().delete()
        # Redirect to order confirmation
        return redirect('order_confirmation', order_id=order.id)

    context = {
        'cart': cart,
        'cart_items': cart.items.all()
    }
    return render(request, 'main/checkout.html', context)

@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'main/order_confirmation.html', {'order': order})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'main/order_history.html', {'orders': orders})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome back!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'main/login.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')

@login_required
def reservations(request):
    user_reservations = Reservation.objects.filter(user=request.user).order_by('-date', '-time')
    return render(request, 'main/reservations.html', {
        'reservations': user_reservations
    })

@require_POST
@login_required
def cancel_reservation(request, reservation_id):
    try:
        reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
        if reservation.status == 'pending':
            reservation.status = 'cancelled'
            reservation.save()
            return JsonResponse({
                'status': 'success',
                'message': 'Reservation cancelled successfully'
            })
        else:
            return JsonResponse({
                'status': 'error',
                'message': 'Cannot cancel a reservation that is not pending'
            }, status=400)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400) 