import pytest

from exercises_app.models import Product


@pytest.mark.django_db
def test_get_product_view(product, client):
    response = client.get(f'/product/{product.pk}/')
    assert response.status_code == 200

@pytest.mark.parametrize('key, value', (
        ('name', 'fake name'),
        ('description', 'lorem ipsum description'),
        ('price', 22.50),
    )
)
@pytest.mark.django_db
def test_product_view_context(key, value, product, client):
    response = client.get(f'/product/{product.pk}/')
    assert response.context[key] == value

@pytest.mark.django_db
def test_product_view_add(client):
    response = client.post(f'/product/add/', {
        'name': 'fake name',
        'description': 'lorem ipsum description',
        'price': 22.50,
    })
    assert response.status_code == 302

@pytest.mark.django_db
def test_product_view_model_exist(client):
    client.post(f'/product/add/', {
        'name': 'fake name',
        'description': 'lorem ipsum description',
        'price': 22.50,
    })
    product = Product.objects.filter(
        name='fake name',
        description='lorem ipsum description',
        price=22.50,
    )
    assert product


@pytest.mark.django_db
def test_product_view_list_status(client):
    response = client.get('/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_product_view_list(add_three_product, client):
    response = client.get('/')
    for i in range(3):
        assert response.context['products'][i].name == add_three_product[i].name