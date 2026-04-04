import stripe
from django.conf import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


from products.models import PhotoProduct
from bookings.models import Photoshoot
from .models import Order, PurchasedPhoto

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def create_checkout_session(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty.")
        return redirect('view_cart')

    line_items = []
    product_ids = []
    session_ids = []

    for item_key, quantity in cart.items():
        if item_key.startswith('p_'):  # Фото
            item_id = item_key.split('_')[1]
            product = get_object_or_404(PhotoProduct, pk=item_id)
            product_ids.append(item_id)
            line_items.append({
                'price_data': {
                    'currency': 'eur',
                    'unit_amount': int(product.price * 100),
                    'product_data': {
                        'name': product.title,
                        'images': [f"https://res.cloudinary.com/drscildms/image/upload/v1/{product.preview_image}"],
                    },
                },
                'quantity': 1,
            })
        elif item_key.startswith('s_'):  # Сесія
            item_id = item_key.split('_')[1]
            photoshoot = get_object_or_404(Photoshoot, pk=item_id)
            session_ids.append(f"{item_id}:{quantity}")
            line_items.append({
                'price_data': {
                    'currency': 'eur',
                    'unit_amount': int(photoshoot.deposit_price * 100),
                    'product_data': {
                        'name': f"Deposit: {photoshoot.title}",
                        'description': photoshoot.expected_dates,
                    },
                },
                'quantity': quantity,
            })

    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            locale='en',
            success_url=request.build_absolute_uri(
                reverse('checkout_success')) + "?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=request.build_absolute_uri(reverse('view_cart')),
            metadata={
                'product_ids': ",".join(product_ids),
                'session_data': ",".join(session_ids),
                'user_id': request.user.id # Тепер ми впевнені, що юзер залогінений
            }
        )
        return redirect(checkout_session.url, code=303)
    except Exception as e:
        messages.error(request, f"Stripe error: {str(e)}")
        return redirect('view_cart')


def checkout_success(request):
    if 'cart' in request.session:
        del request.session['cart']
    return render(request, 'checkout/success.html')


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WH_SECRET
        )
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        
        user_id = session['metadata'].get('user_id')
        product_ids = session['metadata'].get('product_ids', "").split(',')

        if user_id:
            user = User.objects.get(id=user_id)
            
            
            order = Order.objects.create(
                user=user,
                total=session['amount_total'] / 100,
                status="paid",
                stripe_session_id=session['id']
            )

            
            for p_id in product_ids:
                if p_id:
                    product = PhotoProduct.objects.get(id=p_id)
                    PurchasedPhoto.objects.get_or_create(
                        user=user,
                        product=product,
                        order=order
                    )
            
            print(f"✅ Payment successful for user {user.username}. Order created.")

    return HttpResponse(status=200)