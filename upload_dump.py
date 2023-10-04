from datetime import datetime

from baselayer.database import SessionLocal
from baselayer.models import Product, Sale, Inventory, Category  # Import your models from the appropriate module

session = SessionLocal()


# Insert dummy data into the 'products' table

def create_dummy_categories():
    # Check if any entries exist in the Category model
    if not session.query(Category).count():
        categories = [
            Category(name="Category A"),
            Category(name="Category B"),
            Category(name="Category C"),
        ]
        session.add_all(categories)
        session.commit()
    else:
        print("Categories already exist. Skipping creation.")


def create_dummy_products():
    # Check if any entries exist in the Product model
    if not session.query(Product).count():
        products = [
            Product(name="Product 1", description="Description for Product 1", price=19.99, category_id=1),
            Product(name="Product 2", description="Description for Product 2", price=29.99, category_id=2),
            Product(name="Product 3", description="Description for Product 3", price=9.99, category_id=3),
        ]
        session.add_all(products)
        session.commit()
    else:
        print("Products already exist. Skipping creation.")


# Insert dummy data into the 'sales' table
def create_dummy_sales():
    # Check if any entries exist in the Sale model
    if not session.query(Sale).count():
        sales = [
            Sale(sale_date=datetime(2023, 10, 1, 10, 0, 0), quantity=5, total_price=99.95, product_id=1),
            Sale(sale_date=datetime(2023, 10, 2, 11, 30, 0), quantity=2, total_price=59.98, product_id=2),
            Sale(sale_date=datetime(2023, 10, 3, 14, 15, 0), quantity=3, total_price=29.97, product_id=3),
        ]
        session.add_all(sales)
        session.commit()
    else:
        print("Sales already exist. Skipping creation.")


# Insert dummy data into the 'inventory' table
def create_dummy_inventory():
    # Check if any entries exist in the Inventory model
    if not session.query(Inventory).count():
        inventory = [
            Inventory(product_id=1, quantity=10),
            Inventory(product_id=2, quantity=20),
            Inventory(product_id=3, quantity=15),
        ]
        session.add_all(inventory)
        session.commit()
    else:
        print("Inventory records already exist. Skipping creation.")


# Call the functions to populate the tables
if __name__ == "__main__":
    create_dummy_products()
    create_dummy_sales()
    create_dummy_inventory()
