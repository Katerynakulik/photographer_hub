from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import PhotoProduct
from bookings.models import Photoshoot

def view_cart(request):
    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """
    Universal view to add either a Photo or a Photoshoot Deposit to the cart.
    Expects 'item_type' (product/session) from the POST request.
    """
    cart = request.session.get('cart', {})
    item_type = request.POST.get('item_type', 'product') # Default to product
    
    if item_type == 'session':
        item = get_object_or_404(Photoshoot, pk=item_id)
        item_key = f"s_{item_id}"
        display_name = f"Waitlist: {item.title}"
    else:
        item = get_object_or_404(PhotoProduct, pk=item_id)
        item_key = f"p_{item_id}"
        display_name = item.title

    if item_key not in cart:
        cart[item_key] = 1
        messages.success(request, f"Success! {display_name} added to your cart.")
    else:
        messages.info(request, f"{display_name} is already in your cart.")
    
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