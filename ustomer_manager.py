from config import CUSTOMER_FILE
from storage import load_data, save_data
from utils import generate_id, find_by_id


def add_customer():
    customers = load_data(CUSTOMER_FILE)

    name = input("Customer Name: ").strip()
    phone = input("Phone Number: ").strip()
    address = input("Address: ").strip()

    if not all([name, phone, address]):
        print("All fields are required.")
        return

    customer = {
        "id": generate_id("CUS"),
        "name": name,
        "phone": phone,
        "address": address
    }

    customers.append(customer)
    save_data(CUSTOMER_FILE, customers)

    print("Customer added successfully!")
    print("Customer ID:", customer["id"])


def view_customers():
    customers = load_data(CUSTOMER_FILE)

    if not customers:
        print("No customers found.")
        return

    for customer in customers:
        print("-" * 40)
        print("ID:", customer["id"])
        print("Name:", customer["name"])
        print("Phone:", customer["phone"])
        print("Address:", customer["address"])


def search_customer():
    customer_id = input("Enter Customer ID: ").strip()

    customers = load_data(CUSTOMER_FILE)
    customer = find_by_id(customers, customer_id)

    if customer:
        for key, value in customer.items():
            print(f"{key}: {value}")
    else:
        print("Customer not found.")
