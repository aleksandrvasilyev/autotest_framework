from my_framework.hw.db.alchemy.models.products import Products
from my_framework.hw.db.alchemy.session import session


class ProductsRepository:

    def __init__(self):
        self.__session = session
        self.__model = Products

    def get_product_by_id(self, product_id):
        product = self.__session.get(self.__model, {'id': product_id})
        return product

    def get_all(self):
        all_products = self.__session.query(self.__model).all()
        # for product in all_products:
        #     print(f"{product}")
        return all_products

    def add_product(self, product: Products):
        self.__session.add(product)
        self.__session.commit()

    def delete_product_by_id(self, product: id):
        product = self.get_product_by_id(product)
        self.__session.delete(product)
        self.__session.commit()
