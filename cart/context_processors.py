from .cart import Cart


# create context processor so out cart can worl on all pages
def cart(request):
    # return the default data from our cart
    return {"cart": Cart(request)}
