from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import PhotoProduct

def view_cart(request):
    cart = request.session.get("cart", {})
    products = PhotoProduct.objects.filter(id__in=cart.keys())
    total = sum(p.price for p in products)
    return render(request, "cart/cart.html", {"products": products, "total": total})

def add_to_cart(request, product_id):
    """ Додає товар у сесію кошика """
    product = get_object_or_404(PhotoProduct, id=product_id)
    cart = request.session.get('cart', {})

    # Додаємо товар (або збільшуємо кількість, хоча для фото зазвичай 1)
    if product_id in list(cart.keys()):
        messages.info(request, f"{product.title} вже у вашому кошику.")
    else:
        cart[product_id] = 1
        messages.success(request, f"Додано {product.title} у кошик!")

    request.session['cart'] = cart
    return redirect(request.META.get('HTTP_REFERER', 'home'))