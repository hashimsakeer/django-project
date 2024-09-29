from django.shortcuts import render, get_object_or_404, redirect
from .models import Product,Category,Cart,CartItem


def index(request):
    category=Category.objects.all()
    return render(request,'home.html',{'category': category})
def cat_pro_list(request,category_id):
    category=get_object_or_404(Category,id=category_id)
    products=Product.objects.filter(category=category)
    return render(request,'products.html',{'category':category,'products':products})

def product_detail(request,product_id):
    products=get_object_or_404(Product,id=product_id)
    return render(request,'product_detail.html',{'products':products})

def searchresult(request):
    query = request.GET.get('q')
    results = Product.objects.filter(name__icontains=query)
    return render(request, 'search.html', {'query':query,'results': results})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('ecommerce:cart_page')

def cart_page(request):
    cart = Cart.objects.filter(user=request.user).first()
    cart_items = CartItem.objects.filter(cart=cart) if cart else []
    return render(request, 'cart.html', {'cart_items': cart_items})

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('ecommerce:cart_page')
