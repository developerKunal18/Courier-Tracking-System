from config import SHIPMENT_FILE, SHIPMENT_STATUSES
from storage import load_data


def shipment_statistics():
    shipments = load_data(SHIPMENT_FILE)

    print("\n========== COURIER REPORT ==========")

    print("Total Shipments:", len(shipments))

    for status in SHIPMENT_STATUSES:
        count = sum(
            1 for shipment in shipments
            if shipment["status"] == status
        )

        print(f"{status}: {count}")

    total_revenue = sum(
        shipment["delivery_charge"]
        for shipment in shipments
        if shipment["status"] == "Delivered"
    )

    print("Delivered Shipment Revenue: ₹", round(total_revenue, 2))

    print("=" * 36)


def pending_deliveries():
    shipments = load_data(SHIPMENT_FILE)

    pending = [
        shipment for shipment in shipments
        if shipment["status"] not in ["Delivered", "Cancelled"]
    ]

    if not pending:
        print("No pending deliveries.")
        return

    print("\n========== PENDING DELIVERIES ==========")

    for shipment in pending:
        print("-" * 40)
        print("Tracking ID:", shipment["tracking_id"])
        print("Receiver:", shipment["receiver"])
        print("Status:", shipment["status"])
        print("Destination:", shipment["destination"])
