from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import PhotoProduct

def view_cart(request):
    """ Сторінка, яка відображає вміст кошика """
    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Додає товар і показує гарний тост """
    product = get_object_or_404(PhotoProduct, pk=item_id)
    cart = request.session.get('cart', {})

    if item_id not in list(cart.keys()):
        cart[item_id] = 1
        messages.success(request, f"Success! {product.title} added to your cart.")
    
    request.session['cart'] = cart
    return redirect(request.POST.get('redirect_url', reverse('home')))

def remove_from_cart(request, item_id):
    """ Видалення товару з кошика (з тостом) """
    product = get_object_or_404(PhotoProduct, pk=item_id)
    cart = request.session.get('cart', {})
    
    if item_id in cart:
        cart.pop(item_id)
        messages.success(request, f"Removed {product.title} from your cart.")
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))