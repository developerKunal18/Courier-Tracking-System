from config import SHIPMENT_FILE, SHIPMENT_STATUSES
from storage import load_data, save_data
from utils import find_by_id, current_datetime


def update_shipment_status():
    shipments = load_data(SHIPMENT_FILE)

    tracking_id = input("Tracking ID: ").strip()

    shipment = find_by_id(
        shipments,
        tracking_id,
        "tracking_id"
    )

    if not shipment:
        print("Shipment not found.")
        return

    if shipment["status"] in ["Delivered", "Cancelled"]:
        print("This shipment is already closed.")
        return

    print("\nAvailable Statuses:")

    for index, status in enumerate(SHIPMENT_STATUSES, 1):
        print(f"{index}. {status}")

    try:
        choice = int(input("Select Status: "))

        if not 1 <= choice <= len(SHIPMENT_STATUSES):
            print("Invalid choice.")
            return

    except ValueError:
        print("Invalid input.")
        return

    new_status = SHIPMENT_STATUSES[choice - 1]

    current_index = SHIPMENT_STATUSES.index(shipment["status"])
    new_index = SHIPMENT_STATUSES.index(new_status)

    if new_status == shipment["status"]:
        print("Shipment already has this status.")
        return

    if new_status != "Cancelled" and new_index != current_index + 1:
        print("Shipment must follow the delivery status sequence.")
        return

    if new_status == "Delivered" and not shipment["agent_id"]:
        print("Assign a delivery agent before delivery.")
        return

    shipment["status"] = new_status

    shipment["history"].append({
        "status": new_status,
        "timestamp": current_datetime()
    })

    save_data(SHIPMENT_FILE, shipments)

    print("Shipment status updated successfully!")


def track_shipment():
    tracking_id = input("Enter Tracking ID: ").strip()

    shipments = load_data(SHIPMENT_FILE)

    shipment = find_by_id(
        shipments,
        tracking_id,
        "tracking_id"
    )

    if not shipment:
        print("Tracking ID not found.")
        return

    print("\n========== SHIPMENT TRACKING ==========")

    print("Tracking ID:", shipment["tracking_id"])
    print("Receiver:", shipment["receiver"])
    print("Destination:", shipment["destination"])
    print("Current Status:", shipment["status"])

    print("\nTracking History:")

    for event in shipment["history"]:
        print(
            f"{event['timestamp']} - {event['status']}"
        )

    print("=" * 39)
