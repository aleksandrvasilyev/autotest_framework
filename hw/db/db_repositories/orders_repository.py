import psycopg2


class OrdersRepository:
    def __init__(self):
        self.__connection = psycopg2.connect(user='postgres',
                                             password='123',
                                             host='127.0.0.1',
                                             port='5432',
                                             database='store')
        self.__connection.set_session(autocommit=True)
        self.__cursor = self.__connection.cursor()

    def get_all(self):
        self.__cursor.execute("select * from products;")
        return self.__cursor.fetchall()

    def get_product_by_id(self, product_id):
        self.__cursor.execute(f"select * from products where products.id = {product_id};")
        return self.__cursor.fetchone()

    def insert_one(self, name, price):
        self.__cursor.execute(f"insert into products (name, price) values ('{name}', '{price}');")
        # self.__connection.commit()

    def delete_by_id(self, product_id):
        self.__cursor.execute(f"delete from products where products.id = '{product_id}'")
        # self.__connection.commit()

    def __del__(self):
        if self.__connection:
            if self.__cursor:
                self.__cursor.close()
            self.__connection.close()
