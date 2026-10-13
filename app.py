from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

products =[
    
  {
    "id": 1,
    "name": "Milk",
    "price": 80,
    "quantity": 20
  },
  {
    "id": 2,
    "name": "Bread",
    "price": 65,
    "quantity": 10
  }

]

@app.route("/")
def home():
    return jsonify({
        "Message": "Inventory Management API is running!"
        
    })

@app.route("/api/products", methods=["GET", "POST"])
def list_products():
    visit =request.method
    if visit == "GET":
        return jsonify(products)
        
    data = request.get_json()
    if not data or not data.get("name"):
        return jsonify({"error": "Product name is required"}), 400 
    
    if float(data["price"]) < 0 or int(data["quantity"]) < 0:
        return jsonify({"error": "Price and quantity cannot be negative"}), 400

    new_id = max(
     product["id"] for product in products
    ) + 1

    new_product = {
        "id": new_id,
        "name": data["name"],
        "price": data["price"],
        "quantity": data["quantity"]
    }
    products.append(new_product)

    return jsonify(new_product), 201

@app.route("/api/products/<int:product_id>", methods=["PATCH"])
def update_product(product_id):
    data = request.get_json()
    for product in products:
        if product["id"] == product_id:
            product["quantity"]= data["quantity"]
            return jsonify(product), 200
    else:
        return jsonify({"Message": "Product not found"}), 404
        
@app.route("/api/products/<int:product_id>", methods= ["DELETE"])
def delete_product(product_id):
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            return jsonify({"Message": "product deleted successfully"}), 200
    else:
        return jsonify({"message": "Product not found"}), 404

@app.route("/api/external-product/<barcode>", methods=["GET"])
def get_external_product(barcode):
    url = f"https://world.openfoodfacts.org/api/v2/product/{barcode}.json"

    try:
        response = requests.get(
        url,
        headers={"User-Agent": "InventoryManagementStudent/1.0"},
        timeout=10
        )
        response.raise_for_status()
        data = response.json()

        if data.get("status") != 1:
            return jsonify({"error": "Product not found"}), 404

        product = data.get("product", {})

        return jsonify({
            "name": product.get("product_name", "Unknown"),
            "barcode": barcode,
            "brand": product.get("brands", "Unknown")
        }), 200

    except requests.RequestException as error:
        return jsonify({
        "error": "External API unavailable",
        "details": str(error)
    }), 502


if __name__ == "__main__":
    app.run(debug=True)
