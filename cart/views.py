from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages


def cart_summary(request):
    # get the cart
    cart = Cart(request)
    cart_products = cart.get_products
    quantities = cart.get_quantities
    totals = cart.cart_total()

    return render(
        request,
        "cart_summary.html",
        {
            "cart_products": cart_products,
            "quantities": quantities,
            "totals": totals,
        },
    )


def cart_add(request):
    # Get the cart

    cart = Cart(request)

    # test for POST
    if request.POST.get("action") == "post":
        # get stuff
        product_id = int(request.POST.get("product_id"))
        product_qty = int(request.POST.get("product_qty"))

        # loodup product in DB
        product = get_object_or_404(Product, id=product_id)
        # save to session
        cart.add(product=product, quantity=product_qty)

        # get cart count
        cart_quantity = cart.__len__()

        # retuen response
        response = JsonResponse({"qty": cart_quantity})
        messages.success(request, "Product add to cart")

        # response = JsonResponse({"Product Name: ": product.name})
        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        # get stuff
        product_id = int(request.POST.get("product_id"))
        # call the delete function in cart
        cart.delete(product=product_id)
        response = JsonResponse({"product": product_id})
        messages.success(request, "Item deleted from cart")

        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        # get stuff
        product_id = int(request.POST.get("product_id"))
        product_qty = int(request.POST.get("product_qty"))
        cart.update(product=product_id, quantity=product_qty)
        response = JsonResponse({"qty": product_qty})
        messages.success(request, "Product quantity updated")

        return response
        # return redirect("cart_summary")
