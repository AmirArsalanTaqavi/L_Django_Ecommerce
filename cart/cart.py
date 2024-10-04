from store.models import Product,Profile cart


class Cart:
    def __init__(self, request):
        self.session = request.session

        # Get request
        self.request = request

        # Get the current session key if it exist
        cart = self.session.get("session_key")

        # if the user is new, no session key! create one
        if "session_key" not in request.session:
            cart = self.session["session_key"] = {}

        # Make sure cart is available on all plages of website
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

        # Deal with logged in user
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # convert single quatation to double
            carty = str(self.cart)
            carty = cart.replace("\'","\"")

    def cart_total(self):
        # Get product IDS
        product_ids = self.cart.keys()
        # lookup those keys in our products database model
        products = Product.objects.filter(id__in=product_ids)
        # Get quantities
        quantities = self.cart

        total = 0
        for key, value in quantities.items():
            # convert key string to int
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total += product.sale_price * value
                    else:
                        total += product.price * value
        return total

    def get_products(self):
        # get ids from cart
        product_ids = self.cart.keys()
        # use ids to lookup products in database model
        products = Product.objects.filter(id__in=product_ids)
        # return the products in database model
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

    def delete(self, product):
        product_id = str(product)
        # delete from dictonary
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True
