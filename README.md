# E-commerce Admin Dashboard API

The E-commerce Admin Dashboard API is a powerful back-end solution designed to support e-commerce businesses in managing their operations effectively. This API serves as the core component for an admin dashboard, providing essential features and functionalities for e-commerce managers and administrators.

## Key Features

- **Sales Insights:** Retrieve, filter, and analyze sales data. Analyze revenue on a daily, weekly, monthly, and annual basis. Compare revenue across different periods and categories. Provide sales data by date range, product, and category.

- **Inventory Management:** View current inventory status, including low stock alerts. Update inventory levels and track changes over time.

- **Product Management:** Add new products to the e-commerce catalog, categorize products, and efficiently search for products.

## Technology Stack

- **Programming Language:** Python
- **Web Framework:** FastAPI
- **Database:** PostgreSQL (or other preferred databases)
- **API Documentation:** Swagger or ReDoc (auto-generated)

## Project Goals

- Develop a robust and scalable back-end API for e-commerce administrators.
- Provide valuable insights and analytics tools for data-driven decisions.
- Create a user-friendly API with well-documented endpoints.

## Getting Started

To get started with this API, follow these steps:

### Prerequisites

- Python (version X.X.X)
- PostgreSQL database (or other preferred databases)

### Installation


The first thing to do is to clone the repository:
```shell
git clone "enter_here_link"
```
Create a virtual environment to install dependencies in and activate it:
run following command to install python-env

```shell
sudo apt-get install python3-venv  
mkdir venv
```

create and activate virtual environment

```shell
python3 -m venv venv 
source venv/bin/activate 
```
Then install the dependencies:

```shell
pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal

### Database Setup

Create a database in PostgreSQL (or other preferred databases) and update the database credentials in the database file.

### Running the API

Once `uvicorn` is installed, run the API with the following command:

```shell
uvicorn main:app --reload
```

The API will then be available at `http://localhost:8000`.

## Run the script

```shell
python3 upload_dump.py
```
Above script will upload the dummy data to the database

Now head to `http://localhost:8000/docs` to view the Swagger UI and interact with the API.