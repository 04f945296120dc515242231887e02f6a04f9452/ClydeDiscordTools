import sqlite3


class Database:
    """
    A class representing a SQLite database.
    """
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        """
        Create a table in the database with the given name and columns.
        """
        col_str = ', '.join([f'{col_name} {col_type}' for col_name, col_type in columns])
        create_table_query = f'CREATE TABLE IF NOT EXISTS {table_name} ({col_str});'
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def drop_table(self, table_name):
        """
        Drop a table from the database with the given name.
        """
        drop_table_query = f'DROP TABLE IF EXISTS {table_name};'
        self.cursor.execute(drop_table_query)
        self.conn.commit()

    def insert_data(self, table_name, data):
        """
        Insert data into a table in the database.
        """
        values = ', '.join(['?' for _ in range(len(data))])
        insert_data_query = f'INSERT INTO {table_name} VALUES ({values});'
        self.cursor.execute(insert_data_query, data)
        self.conn.commit()

    def select_data(self, table_name, columns, where=None):
        """
        Select data from a table in the database with the given columns and WHERE clause.
        """
        col_str = ', '.join(columns)
        select_data_query = f'SELECT {col_str} FROM {table_name}'
        if where is not None:
            clause = f'WHERE {where}'
            select_data_query += f' {clause}'
        self.cursor.execute(select_data_query)
        return self.cursor.fetchall()

    def close(self):
        """
        Close the database connection.
        """
        self.conn.close()
