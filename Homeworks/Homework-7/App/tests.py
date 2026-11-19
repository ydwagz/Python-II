from django.test import TestCase
from .models import Product


class ProductsPageTests(TestCase):
    def test_displays_product_names(self):
        Product.objects.create(name='Test product', description='A test product', price='9.99')

        response = self.client.get('/products/')

        self.assertContains(response, 'Test product')

    def test_displays_message_when_there_are_no_products(self):
        response = self.client.get('/products/')

        self.assertContains(response, 'No products available.')

    def test_product_name_links_to_details_page(self):
        product = Product.objects.create(name='Test product', description='A test product', price='9.99')

        response = self.client.get('/products/')

        self.assertContains(response, f'href="/products/{product.id}/"')

    def test_product_details_page_shows_product_fields(self):
        product = Product.objects.create(name='Test product', description='A test description', price='9.99')

        response = self.client.get(f'/products/{product.id}/')

        self.assertContains(response, 'Test product')
        self.assertContains(response, 'A test description')
        self.assertContains(response, '9.99')
