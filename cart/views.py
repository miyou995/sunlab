from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import TemplateView
from django.views.decorators.http import require_POST
from .cart import Cart
from core.models import Product
from delivery.models import Wilaya
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from .forms import CartAddProductForm
from django.template.loader import render_to_string
from django.contrib import messages
from django.core import serializers
from coupons.models import Coupon
    
# class CheckoutView(TemplateView):
#     template_name = "checkout.html"

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'override': True})
        # print('baskets details', list(cart))
        # print('Wach ahda item details', item)
    # for item in cart:
    #     item['update_quantity_form'] = CartAddProductForm(initial={ 'quantity': item['quantity']})
    #     item['total'] = item['product'].price * item['quantity']
    #     items.append(item)
    #     products.append(item['product'])
    context = {
        'cart': cart,
        # 'coupon_apply_form': coupon_apply_form
    }
    for item in cart:
        print('itrem', item)
    return render(request, 'cart.html', context)

# def cart_add_one_product(request):
#     cart = Cart(request)
#     # product_id = request.POST['product_id']
#     # Get the product that we want to add
#     p_id = request.GET.get('product_id')
#     print('request', p_id)
#     product = get_object_or_404(Product, id=p_id, actif=True)
#     tailles = product.taille.all()
#     colors = product.couleur.all()

#     print('les couleurs', colors)
#     pointures = product.pointure.all()
#     if tailles:
#         taille = tailles[0]
#     color = colors.first()
#     print('les couleurs', color)

#     if pointures:
#         pointure = pointures[0]
#     if product:
#         quantity = 1
#         try:
#             print('pointure',pointure)
#         except:
#             pass
#         try:
#             print('taille', taille)
#         except:
#             pass
#         try:
#             print(color, 'taille, pointure')
#         except:
#             pass
        
        
#         try:
#             cart.add(
#                 product=product,
#                 quantity=quantity,
#                 pointure = pointure,
#                 color = color
#             ) 
#         except:
#             try:
#                 cart.add(
#                     product=product,
#                     quantity=quantity,
#                     taille = taille,
#                     color = color
#                 )
#             except:
#                 cart.add(
#                     product=product,
#                     quantity=quantity,
#                     color = color
#                 )
#     return JsonResponse(serializers.serialize('json', color), safe=True)

    # if tailles:
    #     taille = tailles[0]
    #     cart.add(taille = taille)

    # else:
    #     taille = False
    # if colors:
    #     color = colors[0]
    #     cart.add(color = color)
    # else:
    #     color = False
    # if pointures:
    #     pointure = pointures[0]
    #     cart.add(pointure = pointure)
    # else:
    #     pointure = False

    # else:
        # return redirect('cart:cart_detail')

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    print('the Cart ')
    try:
        print('the Cart ')

        if form.is_valid():
                cd = form.cleaned_data
                print('cd', cd)
                cart.add(
                    product=product,
                    quantity=cd['quantity'],
                    override_quantity=cd['override'],
                    parfum=cd['parfum'],
                    cheveux=cd['cheveux'],
                )
                print('the Cart two', cart)
                return redirect('cart:cart_detail')
    except:
        print('NOOOOOOOO')
        return redirect('/')

@require_POST
def cart_update(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity'))
    cart.update(product=product, quantity=quantity)
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')
