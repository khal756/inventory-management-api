# Inventory Management System API

## Description
This project is an inventory management API built using Python and Flask. It allows users to manage products and get product information from the Open Food Facts API.

## Technologies Used
- Python
- Flask
- Requests
- Pytest
- Git and GitHub

## Features
- View all products.
- Add new products.
- Update product quantities.
- Delete products.
- Search for external products using a barcode.
- Import external products into inventory.
- Manage inventory using a command-line interface.
- Validate product input.
- Return appropriate HTTP status codes.

## How to Run the Project

1. Activate the virtual environment:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

2. Install the required packages:

   ```powershell
   python -m pip install Flask requests pytest
   ```

3. Start the API:

   ```powershell
   python app.py
   ```

4. To run the command-line interface, open another terminal and run:

   ```powershell
   python cli.py
   ```

## API Endpoints
- `GET /` – Check if the API is running.
- `GET /api/products` – View all products.
- `POST /api/products` – Add a product.
- `PATCH /api/products/<product_id>` – Update product quantity.
- `DELETE /api/products/<product_id>` – Delete a product.
- `GET /api/external-product/<barcode>` – Get external product information.
- `POST /api/import-product/<barcode>` – Import an external product into inventory.

## Testing
I used Pytest to test the API. All 7 tests passed.

The tests cover:
- The home endpoint.
- Retrieving products.
- Adding a product.
- Updating product quantity.
- Deleting a product.
- Handling a product that does not exist.
- Importing an external product.

Run the tests using:

```powershell
python -m pytest -v
```

## Conclusion
This project helped me practise building REST APIs with Flask, performing CRUD operations, integrating an external API, creating a CLI, and writing automated tests.

**Note:** Products are stored in a Python list, so changes are not permanently saved when the application restarts.
