from django.shortcuts import get_object_or_404
from products.models import PhotoProduct
from bookings.models import Photoshoot

def cart_contents(request):
    cart_items = []
    total = 0
    product_count = 0 
    cart = request.session.get('cart', {})

    for item_key, quantity in cart.items():
        if item_key.startswith('p_'):
            # Photos: Digital License (Strictly 1)
            item_id = item_key.split('_')[1]
            try:
                product = PhotoProduct.objects.get(pk=item_id)
                subtotal = product.price
                cart_items.append({
                    'item_key': item_key,
                    'display_title': product.title,
                    'display_price': product.price,
                    'subtotal': subtotal,
                    'display_image': product.preview_image,
                    'quantity': 1,
                    'type': 'photo'
                })
                total += subtotal
                product_count += 1 
            except PhotoProduct.DoesNotExist:
                continue
        
        elif item_key.startswith('s_'):
            # Sessions: Deposit (Can be multiple people)
            item_id = item_key.split('_')[1]
            try:
                session = Photoshoot.objects.get(pk=item_id)
                subtotal = session.deposit_price * quantity
                cart_items.append({
                    'item_key': item_key,
                    'display_title': session.title,
                    'display_price': session.deposit_price,
                    'subtotal': subtotal,
                    'display_image': session.image,
                    'quantity': quantity,
                    'type': 'session'
                })
                total += subtotal
                product_count += quantity
            except Photoshoot.DoesNotExist:
                continue

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count, 
    }

    return context