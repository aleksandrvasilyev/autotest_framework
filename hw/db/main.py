from my_framework.hw.db.db_repositories.orders_repository import OrdersRepository

orders_repo = OrdersRepository()

print(orders_repo.get_all())

# print(orders_repo.get_product_by_id(1))
orders_repo.insert_one('gaming laptop', '1166')
# orders_repo.delete_by_id(8)

print(orders_repo.get_all())