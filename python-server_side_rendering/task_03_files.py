#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


@app.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Render the items page with data from items.json."""
    try:
        with open('items.json', 'r') as file:
            items_data = json.load(file)
        items_list = items_data.get("items", [])
    except FileNotFoundError:
        items_list = []
    except json.JSONDecodeError:
        items_list = []
    return render_template('items.html', items=items_list)


def read_json_file(filename):
    """Read and parse JSON file."""
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None


def read_csv_file(filename):
    """Read and parse CSV file."""
    try:
        products = []
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert price to float
                if 'price' in row:
                    try:
                        row['price'] = float(row['price'])
                    except ValueError:
                        row['price'] = 0.0
                # Convert id to int
                if 'id' in row:
                    try:
                        row['id'] = int(row['id'])
                    except ValueError:
                        pass
                products.append(row)
        return products if products else []
    except FileNotFoundError:
        return None
    except Exception:
        return None


@app.route('/products')
def products():
    """
    Render the products page with data from JSON or CSV files.
    Query parameters:
    - source: 'json' or 'csv' (required)
    - id: optional product id to filter results
    """
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')
    
    error_message = None
    products_data = []
    
    # Validate source parameter
    if source not in ['json', 'csv']:
        error_message = "Wrong source"
        return render_template('product_display.html', 
                             products=products_data, 
                             error=error_message)
    
    # Read data based on source
    if source == 'json':
        data = read_json_file('products.json')
    else:  # source == 'csv'
        data = read_csv_file('products.csv')
    
    # Handle file reading errors
    if data is None:
        error_message = "File not found or invalid format"
        return render_template('product_display.html', 
                             products=products_data, 
                             error=error_message)
    
    products_data = data
    
    # Filter by id if provided
    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = [p for p in products_data if p.get('id') == product_id]
            
            if not filtered_products:
                error_message = "Product not found"
                products_data = []
            else:
                products_data = filtered_products
        except ValueError:
            error_message = "Invalid product id"
            products_data = []
    
    return render_template('product_display.html', 
                         products=products_data, 
                         error=error_message)


if __name__ == "__main__":
    app.run(debug=True, port=5000)