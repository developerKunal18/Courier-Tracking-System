from config import SHIPMENT_FILE, CUSTOMER_FILE, AGENT_FILE
from storage import load_data, save_data
from utils import (
    generate_id,
    current_datetime,
    find_by_id,
    calculate_delivery_charge
)


def create_shipment():
    customers = load_data(CUSTOMER_FILE)
    shipments = load_data(SHIPMENT_FILE)

    customer_id = input("Sender Customer ID: ").strip()

    customer = find_by_id(customers, customer_id)

    if not customer:
        print("Customer not found.")
        return

    receiver = input("Receiver Name: ").strip()
    receiver_phone = input("Receiver Phone: ").strip()
    destination = input("Delivery Address: ").strip()

    if not all([receiver, receiver_phone, destination]):
        print("Receiver details are required.")
        return

    try:
        weight = float(input("Parcel Weight (KG): "))

        if weight <= 0:
            print("Weight must be greater than zero.")
            return

    except ValueError:
        print("Invalid weight.")
        return

    tracking_id = generate_id("TRK")
    charge = calculate_delivery_charge(weight)

    shipment = {
        "tracking_id": tracking_id,
        "customer_id": customer_id,
        "receiver": receiver,
        "receiver_phone": receiver_phone,
        "destination": destination,
        "weight": weight,
        "delivery_charge": charge,
        "status": "Booked",
        "agent_id": None,
        "created_at": current_datetime(),
        "history": [
            {
                "status": "Booked",
                "timestamp": current_datetime()
            }
        ]
    }

    shipments.append(shipment)
    save_data(SHIPMENT_FILE, shipments)

    print("\nShipment created successfully!")
    print("Tracking ID:", tracking_id)
    print("Delivery Charge: ₹", charge)


def view_shipments():
    shipments = load_data(SHIPMENT_FILE)

    if not shipments:
        print("No shipments found.")
        return

    for shipment in shipments:
        print("-" * 50)
        print("Tracking ID:", shipment["tracking_id"])
        print("Receiver:", shipment["receiver"])
        print("Destination:", shipment["destination"])
        print("Status:", shipment["status"])
        print("Charge: ₹", shipment["delivery_charge"])


def search_shipment():
    tracking_id = input("Enter Tracking ID: ").strip()

    shipments = load_data(SHIPMENT_FILE)

    shipment = find_by_id(
        shipments,
        tracking_id,
        "tracking_id"
    )

    if not shipment:
        print("Shipment not found.")
        return

    for key, value in shipment.items():
        if key != "history":
            print(f"{key}: {value}")


def assign_agent():
    shipments = load_data(SHIPMENT_FILE)
    agents = load_data(AGENT_FILE)

    tracking_id = input("Tracking ID: ").strip()
    agent_id = input("Agent ID: ").strip()

    shipment = find_by_id(
        shipments,
        tracking_id,
        "tracking_id"
    )

    agent = find_by_id(agents, agent_id)

    if not shipment:
        print("Shipment not found.")
        return

    if not agent:
        print("Agent not found.")
        return

    if shipment["status"] in ["Delivered", "Cancelled"]:
        print("Cannot assign an agent to a closed shipment.")
        return

    shipment["agent_id"] = agent_id

    save_data(SHIPMENT_FILE, shipments)

    print("Agent assigned successfully!")
