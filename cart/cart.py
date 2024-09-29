from store.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session

        # Get the current session key if it exist
        cart = self.session.get("session_key")

        # if the user is new, no session key! create one
        if "session_key" not in request.session:
            cart = self.session["session_key"] = {}

        # Make sure cart is avaliable on all plages of website
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        # logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {"price": str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    def get_products(self):
        # get ids from cart
        prodoct_ids = self.cart.keys()
        # use ids to lookup products in database model
        products = Product.objects.filter(id__in=prodoct_ids)
        # retuen the products in database model
        return products

    def __len__(self):
        return len(self.cart)

    def get_quantities(self):
        quantities = self.cart
        return quantities

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        # get cart
        myCart = self.cart
        myCart[product_id] = product_qty

        self.session.modified = True

        updatedCart = self.cart
        return updatedCart
