from product import *


def create_product_table(conn):
    conn.execute('''
        CREATE TABLE PRODUCT
        (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        NAME TEXT NOT NULL, PRICE REAL NOT NULL,
        QUANTITY INTEGER)
        ''')


def insert_new_product(conn, e):
    conn.execute(f'''
    INSERT INTO PRODUCT
    (NAME, PRICE, QUANTITY)
    VALUES
    ('{e.name}', {e.price}, {e.quantity})''')
    conn.commit()


def get_all_products(conn):
    result = conn.execute('SELECT * FROM PRODUCT')
    product_list = []

    for row in result:
        e = Product(row[0], row[1], row[2], row[3])
        product_list.append(e)

    return product_list


def get_product_by_id(conn, id):
    result = conn.execute(f'SELECT * FROM PRODUCT WHERE ID = {id}')

    for row in result:
        e = Product(row[0], row[1], row[2], row[3])

        return e

    return None


def update_product_by_id(conn, e, id):
    conn.execute(f'''UPDATE PRODUCT SET
    NAME = '{e.name}', PRICE = {e.price}, 
    QUANTITY = {e.quantity}
    WHERE ID = {id}''')

    conn.commit()


def delete_product_by_id(conn, id):
    conn.execute(f'DELETE FROM PRODUCT WHERE ID = {id}')
    conn.commit()
