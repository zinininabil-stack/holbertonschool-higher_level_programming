#!/usr/bin/python3
"""Script to create and populate the SQLite database."""

import sqlite3
import os


def create_database():
    """Create the products database and populate it with sample data."""
    db_path = 'products.db'
    
    # Remove existing database if it exists (for fresh start)
    if os.path.exists(db_path):
        os.remove(db_path)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create Products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Insert sample data
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99),
        (3, 'Wireless Mouse', 'Electronics', 29.99),
        (4, 'Desk Lamp', 'Home Goods', 45.00),
        (5, 'USB-C Cable', 'Electronics', 12.99)
    ''')
    
    conn.commit()
    conn.close()
    print(f"Database '{db_path}' created successfully with sample data!")


if __name__ == '__main__':
    create_database()
