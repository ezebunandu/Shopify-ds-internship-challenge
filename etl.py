import os
import sqlite3
import pandas as pd
from sqlalchemy import create_engine


DATA_PATH = "data/"


def copy_csv_to_table(conn, file, table):
    """Copies data from the file into the table using the insert_query"""
    df = pd.read_csv(file, encoding='utf-8', quotechar='|')
    engine = create_engine('sqlite:///orders_data.sqlite', echo=False)
    df.to_sql(table, con=engine, if_exists="append", index=False)


tables = ["Customers", "Categories", "Employees", "OrderDetails",
          "Orders", "Products", "Shippers", "Suppliers"]

files = [os.path.join(DATA_PATH, f"{table}.csv") for table in tables]


def main():
    conn = sqlite3.connect("orders_data.sqlite")

    for file, table in zip(files, tables):
        copy_csv_to_table(conn, file, table)

    conn.close()


if __name__ == "__main__":
    main()
