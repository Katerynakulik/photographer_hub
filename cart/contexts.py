from decimal import Decimal
from products.models import PhotoProduct
from bookings.models import Photoshoot

def cart_contents(request):
    cart_items = []
    total = Decimal('0.00')
    product_count = 0 
    cart = request.session.get('cart', {})

    for item_key, quantity in cart.items():
        try:
            qty = int(quantity)
        except (ValueError, TypeError):
            qty = 1

        if item_key.startswith('p_'):
            item_id = item_key.split('_')[1]
            try:
                product = PhotoProduct.objects.get(pk=item_id)
                # Безпечно отримуємо URL. Якщо фото немає - повертаємо None
                img_url = product.preview_image.url if product.preview_image else None
                
                cart_items.append({
                    'item_key': item_key,
                    'display_title': product.title,
                    'display_price': product.price,
                    'subtotal': product.price,
                    'display_image': product.preview_image if product.preview_image else "",
                    'quantity': 1,
                    'type': 'photo'
                })
                total += product.price
                product_count += 1 
            except (PhotoProduct.DoesNotExist, Exception):
                continue
        
        elif item_key.startswith('s_'):
            item_id = item_key.split('_')[1]
            try:
                session = Photoshoot.objects.get(pk=item_id)
                img_url = session.image.url if session.image else None
                subtotal = session.deposit_price * qty
                
                cart_items.append({
                    'item_key': item_key,
                    'display_title': session.title,
                    'display_price': session.deposit_price,
                    'subtotal': subtotal,
                    'display_image': session.image if session.image else "" ,
                    'quantity': qty,
                    'type': 'session'
                })
                total += subtotal
                product_count += qty
            except (Photoshoot.DoesNotExist, Exception):
                continue

    return {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count, 
    }