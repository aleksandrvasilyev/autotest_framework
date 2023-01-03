from my_framework.hw.db.alchemy.models.orders import Orders
from my_framework.hw.db.alchemy.models.products import Products
from my_framework.hw.db.alchemy.repositories.products_repo import ProductsRepository
from my_framework.hw.db.alchemy.repositories.orders_repo import OrdersRepository
from my_framework.hw.db.alchemy.session import session


ProductsRepository().add_product(Products(name='Meizu note 2', price=430))
ProductsRepository().add_product(Products(name='Samsung x23', price=870))
ProductsRepository().add_product(Products(name='Nokia N101', price=250))
ProductsRepository().add_product(Products(name='Bananas', price=10))
ProductsRepository().add_product(Products(name='Sony xm5', price=350))


OrdersRepository().add_order(Orders(product_id='1', quantity='2'))
OrdersRepository().add_order(Orders(product_id='2', quantity='5'))
OrdersRepository().add_order(Orders(product_id='3', quantity='3'))
OrdersRepository().add_order(Orders(product_id='4', quantity='10'))
OrdersRepository().add_order(Orders(product_id='5', quantity='8'))


result = session.query(Products, Orders).select_from(Products).join(Orders).all()

for product, order in result:
    print(product.name, product.price, order.quantity, order.quantity * product.price)
