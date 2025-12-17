from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Customer Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User, auto_now=True)
    phone = models.CharField(max_length=15, blank=True)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    old_cart = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.user.username


# create a user profile by default when user signs up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()


post_save.connect(create_profile, sender=User)


# Categories of Products
class ProductCategory(models.Model):
    name = models.CharField(max_length=256)
    icon_url = models.URLField(blank=True)
    description = models.TextField()
    parent_category = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        related_name="children_categories",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


# Customer
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Maker
class Maker(models.Model):
    name = models.CharField(max_length=512, unique=True)

    def __str__(self):
        return self.name


# Products
class Product(models.Model):
    class Currency(models.TextChoices):
        USD = ("USD", _("American Dollar"))
        EUR = ("EUR", _("Euro"))
        GBP = ("GBP", _("Pound Sterling"))
        CNY = ("CNY", _("Chinese Yuan"))
        INR = ("INR", _("Indian Rupee"))
        JPY = ("JPY", _("Japanese Yen"))
        KRW = ("KRW", _("South Korean Won"))
        RUB = ("RUB", _("Russian Ruble"))
        IRR = ("IRR", _("Iranian Rial"))
        SEK = ("SEK", _("Swedish Krona"))

    name = models.CharField(max_length=512)
    maker = models.ForeignKey(
        Maker,
        on_delete=models.CASCADE,
        related_name="products",
        blank=True,
        null=True,
    )
    price = models.DecimalField(default=0, max_digits=10, decimal_places=1)
    currency = models.CharField(
        max_length=3,
        choices=Currency.choices,
        default=Currency.USD,
    )
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        related_name="products",
    )
    description = models.CharField(max_length=250, default="", blank=True, null=True)
    image = models.ImageField(upload_to="uploads/products/")
    # Add sales
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, max_digits=10, decimal_places=1)

    def __str__(self):
        return self.name


# Customer Orders
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=200, default="", blank=True, null=True)
    phone = models.CharField(max_length=50, default="", blank=True, null=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product} {self.customer}"
