from my_framework.hw.db.alchemy.models.orders import Orders
from my_framework.hw.db.alchemy.session import session


class OrdersRepository:

    def __init__(self):
        self.__session = session
        self.__model = Orders

    def get_order_by_id(self, order_id):
        order = self.__session.get(self.__model, {'id': order_id})
        return order

    def get_all(self):
        all_orders = self.__session.query(self.__model).all()
        # for product in all_products:
        #     print(f"{product}")
        return all_orders

    def add_order(self, order: Orders):
        self.__session.add(order)
        self.__session.commit()

    def delete_order_by_id(self, order: id):
        order = self.get_order_by_id(order)
        self.__session.delete(order)
        self.__session.commit()
