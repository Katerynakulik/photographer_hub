from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import PhotoProduct

def view_cart(request):
    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    product = get_object_or_404(PhotoProduct, pk=item_id)
    cart = request.session.get('cart', {})
    
    # Mentor Note: Using the 'p_' prefix to match our context processor logic
    item_key = f"p_{item_id}"

    if item_key not in cart:
        cart[item_key] = 1
        messages.success(request, f"Success! {product.title} added to your cart.")
    
    request.session['cart'] = cart
    return redirect(request.POST.get('redirect_url', reverse('home')))

def remove_from_cart(request, item_id):
    """ item_id тут прийде вже як 'p_1' або 's_1' з шаблону кошика """
    cart = request.session.get('cart', {})
    
    if item_id in cart:
        cart.pop(item_id)
        messages.success(request, "Item removed from your cart.")
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))