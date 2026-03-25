# import stripe
from django.conf import settings
from django.shortcuts import redirect

# stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(request):
    cart = request.session.get("cart", {})
    products = PhotoProduct.objects.filter(id__in=cart.keys())
    
    line_items = []
    for product in products:
        line_items.append({
            "price_data": {
                "currency": "eur",
                "product_data": {"name": product.title},
                "unit_amount": int(product.price * 100),
            },
            "quantity": 1,
        })

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=line_items,
        mode="payment",
        success_url=settings.SITE_URL + "/checkout/success/",
        cancel_url=settings.SITE_URL + "/checkout/cancelled/",
        metadata={"user_id": request.user.id}
    )
    return redirect(session.url, code=303)