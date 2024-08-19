from .models import Product
from faker import Faker

faker = Faker()

def create_product():
    return Product.objects.create(
        name=faker.company(),
        price=faker.random_int(min=200, max=9000)
    )
