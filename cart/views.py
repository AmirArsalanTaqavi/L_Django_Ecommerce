from django.shortcuts import render


def cart_summary(request):
    return render(request, "cart_summary.html", {})


# def cart_add(request):
#     return render(request, "cart/add.html")


# def cart_delete(request):
#     pass


# def cart_update(request):
#     pass
