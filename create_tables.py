import sqlite3
from sql_queries import create_table_queries, drop_table_queries


def create_database(db):
    """
    - Creates and connects to the orders_data database
    - Returns the connection
    """
    conn = sqlite3.connect(db)
    conn.text_factory = lambda x: str(x, 'utf-8')
    cur = conn.cursor()
    return cur, conn


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list.
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Drops (if exists) and Creates the orders_data database.
    - Establishes connection with the database and gets
    cursor to it.
    - Drops all the tables.
    - Creates all tables needed.
    - Finally, closes the connection.
    """
    cur, conn = create_database('orders_data.sqlite')
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
