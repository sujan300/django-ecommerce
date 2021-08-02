from django.shortcuts import render,get_object_or_404,HttpResponse
from store.models import Product
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id

# Create your views here.
def store(request, category_slug = None):
    categories = None
    products   = None
    category   = Category.objects.all()

    if category_slug != None:
        categories     = get_object_or_404(Category, slug = category_slug )
        print(f"categories is:{categories}")
        products       = Product.objects.filter(category = categories, is_available= True)
        product_count  = products.count()
    else:
        products      = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    return render(
        request,
        'store/store.html',
        {
            'categories'   :category,
            'products'     :products,
            'product_count':product_count,
        }
    )

def product_detail(request,category_slug,product_slug):
    category   = Category.objects.all()
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug = product_slug)
        in_cart        = CartItem.objects.filter(cart__cart_id=_cart_id(request),product=single_product).exists()
    except Exception as e:
        raise e
    return render(
        request,
        'store/product_detail.html',
        {
            'categories'    :category,
            'single_product':single_product,
            'in_cart'       :in_cart,
        }
    )