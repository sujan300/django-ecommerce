from django.shortcuts import render,redirect,get_object_or_404
from category.models import Category
from store.models import Product
from carts.models import Cart,CartItem

# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_carts(request,product_id):
    product = Product.objects.get(id=product_id) # get single product 
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request)) # get the cart using the cart_id present in the session
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()
    try:
        cart_item = CartItem.objects.get(product = product,cart = cart)
        cart_item.quantity += 1 #increaments of cart_item or cart_item.quantity = cart_item + 1 ## increaments of cart item
        cart_item.save()

    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product  = product,
            quantity = 1,
            cart     = cart,
        )
        cart_item.save()
    return redirect('carts')


def remove_cart(request,product_id):
    cart      = Cart.objects.get(cart_id=_cart_id(request))
    product   = get_object_or_404(Product,id=product_id)
    cart_item = CartItem.objects.get(product=product,cart=cart)
    if cart_item.quantity >1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('carts')

def remove_cart_item(request,product_id):
    cart     = Cart.objects.get(cart_id=_cart_id(request))
    product  = get_object_or_404(Product,id=product_id)
    cart_item= CartItem.objects.get(product=product,cart=cart)
    cart_item.delete()
    return redirect('carts')

def carts(request,total=0,quantity=0,cart_items=None):
    category   = Category.objects.all()
    try:
        cart       = Cart.objects.get(cart_id =_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart,is_active=True)

        for cart_item in cart_items:
            total     +=(cart_item.product.price * cart_item.quantity)
            quantity  +=cart_item.quantity
        tax         = (2*total)/100
        grand_total = total+tax

    except Cart.ObjectNotExist and cart_items.ObjectNotExist:
        pass
    return render(
        request,
        'store/cart.html',
        {
            'categories'   :category,
            'total'        :total,
            'quantity'     :quantity,
            'cart_items'   :cart_items, 
            'tax'          :tax,
            'grand_total'  :grand_total,   
        }
    )
