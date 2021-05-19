import pytest

from django.test import Client

from exercises_app.models import Product


# @pytest.fixture
# def client():
#     return Client()

@pytest.fixture
def product():
    return Product.objects.create(
        name='fake name',
        description='lorem ipsum description',
        price=22.50,
    )

@pytest.fixture
def add_three_product():
    for i in range(3):
        Product.objects.create(
            name=f'fake name {i}',
            description=f'lorem ipsum description {i}',
            price=20.50 + i,
        )
    return Product.objects.all().order_by('name')