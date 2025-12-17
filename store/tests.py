from django.test import TestCase
from .models import Product, ProductCategory, Maker


class ProductModelTest(TestCase):
    def setUp(self):
        self.category = ProductCategory.objects.create(name="Test Category", description="Test")
        self.maker = Maker.objects.create(name="Test Maker")

    def test_product_creation(self):
        product = Product.objects.create(
            name="Test Product",
            maker=self.maker,
            price=10.00,
            category=self.category,
            description="Test description"
        )
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, 10.00)
