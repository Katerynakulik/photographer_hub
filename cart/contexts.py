from django.shortcuts import get_object_or_404
from products.models import PhotoProduct
from bookings.models import Photoshoot

def cart_contents(request):
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_key, quantity in cart.items():
        price = 0  # Default value
        item_data = {}

        try:
            if item_key.startswith('p_'):
                item_id = item_key.split('_')[1]
                product = get_object_or_404(PhotoProduct, pk=item_id)
                price = product.price
                item_data = {'product': product}
                
            elif item_key.startswith('s_'):
                item_id = item_key.split('_')[1]
                session = get_object_or_404(Photoshoot, pk=item_id)
                price = session.deposit_price
                item_data = {'session': session}
            
            else:
                # Mentor Note: If the key is old (no prefix), we skip it to prevent crash
                continue 

            total += quantity * price
            product_count += quantity
            cart_items.append({
                'item_id': item_key,
                'quantity': quantity,
                'price': price,
                **item_data
            })
        except Exception:
            # If product was deleted but stays in session
            continue

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
    }
    return context