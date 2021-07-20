import sqlite3

conn = sqlite3.connect('products.db')


def create_product_table():
    conn.execute('''
        CREATE TABLE PRODUCT
        (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        NAME TEXT NOT NULL, PRICE REAL NOT NULL,
        QUANTITY INTEGER)
        ''')


def insert_into_product_table():
    conn.execute('''
    INSERT INTO PRODUCT
    (NAME, PRICE, QUANTITY)
    VALUES
    ('Pen', 9.99, 6)
    ''')

    conn.execute('''
    INSERT INTO PRODUCT
    (NAME, PRICE, QUANTITY)
    VALUES
    ('Pencil', 8.99, 5)
    ''')

    conn.execute('''
    INSERT INTO PRODUCT
    (NAME, PRICE, QUANTITY)
    VALUES
    ('Book', 12.99, 11)
    ''')

    conn.commit()

    print("success")


def drop_product_table():
    conn.execute("DROP TABLE PRODUCT;")

    conn.commit()


def print_product_table():
    result = conn.execute('SELECT * FROM PRODUCT')

    for row in result:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("PRICE = ", row[2])
        print("QUANTITY = ", row[3])
        print("=========================")


if __name__ == '__main__':
    create_product_table()
    insert_into_product_table()
    print_product_table()
    # drop_product_table()
