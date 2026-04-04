import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from products.models import PhotoProduct
from .models import Order, PurchasedPhoto


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WH_SECRET
        )
    except Exception as e:
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        user_id = session['metadata']['user_id']
        product_ids = session['metadata'].get('product_ids', "").split(',')

        user = User.objects.get(id=user_id)

        order = Order.objects.create(
            user=user,
            total=session['amount_total'] / 100,  # Переводимо з центів
            status="paid",
            stripe_session_id=session['id']
        )

        for p_id in product_ids:
            if p_id:
                product = PhotoProduct.objects.get(id=p_id)
                PurchasedPhoto.objects.create(
                    user=user,
                    product=product,
                    order=order
                )
                
    return HttpResponse(status=200)