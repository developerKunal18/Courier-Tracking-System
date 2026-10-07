import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

CUSTOMER_FILE = os.path.join(DATA_DIR, "customers.json")
AGENT_FILE = os.path.join(DATA_DIR, "agents.json")
SHIPMENT_FILE = os.path.join(DATA_DIR, "shipments.json")

SHIPMENT_STATUSES = [
    "Booked",
    "Picked Up",
    "In Transit",
    "Out for Delivery",
    "Delivered",
    "Cancelled"
]

BASE_DELIVERY_CHARGE = 50
CHARGE_PER_KG = 20
