
import requests

BASE_URL = "http://127.0.0.1:5000/api/products"

def list_products():
    response = requests.get(BASE_URL)
    print(response.status_code, response.json())


def add_product():
    name = input("Product name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    response = requests.post(BASE_URL, json=product)
    print(response.status_code, response.json())


def update_product():
    product_id = int(input("Product ID to update: "))
    quantity = int(input("New quantity: "))

    response = requests.patch(
        f"{BASE_URL}/{product_id}",
        json={"quantity": quantity}
    )
    print(response.status_code, response.json())


def delete_product():
    product_id = int(input("Product ID to delete: "))

    response = requests.delete(f"{BASE_URL}/{product_id}")
    print(response.status_code, response.json())


def main():
    while True:
        print("\n=== Inventory Management ===")
        print("1. List products")
        print("2. Add product")
        print("3. Update product quantity")
        print("4. Delete product")
        print("5. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                list_products()
            elif choice == "2":
                add_product()
            elif choice == "3":
                update_product()
            elif choice == "4":
                delete_product()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Choose 1–5.")
        except (ValueError, requests.RequestException) as error:
            print("Something went wrong:", error)


if __name__ == "__main__":
    main()
