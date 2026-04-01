from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import PhotoProduct

def view_cart(request):
    """ Сторінка перегляду вмісту кошика """
    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Додавання товару в кошик """
    product = get_object_or_404(PhotoProduct, pk=item_id)
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        messages.info(request, f"{product.title} is already in your cart.")
    else:
        cart[item_id] = 1
        messages.success(request, f"Added {product.title} to your cart!")

    request.session['cart'] = cart
    return redirect(request.POST.get('redirect_url', reverse('home')))

def remove_from_cart(request, item_id):
    """ Видалення товару """
    try:
        cart = request.session.get('cart', {})
        product = get_object_or_404(PhotoProduct, pk=item_id)
        cart.pop(item_id)
        messages.success(request, f"Removed {product.title} from your cart")
        request.session['cart'] = cart
        return redirect(reverse('view_cart'))
    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return redirect(reverse('view_cart'))