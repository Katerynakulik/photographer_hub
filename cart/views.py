from django.shortcuts import render, redirect, get_object_or_404
from products.models import PhotoProduct

def view_cart(request):
    cart = request.session.get("cart", {})
    products = PhotoProduct.objects.filter(id__in=cart.keys())
    total = sum(p.price for p in products)
    return render(request, "cart/cart.html", {"products": products, "total": total})

def add_to_cart(request, product_id):
    cart = request.session.get("cart", {})
    cart[str(product_id)] = 1
    request.session["cart"] = cart
    return redirect("view_cart")