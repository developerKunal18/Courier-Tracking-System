from customer_manager import (
    add_customer,
    view_customers,
    search_customer
)

from agent_manager import (
    add_agent,
    view_agents,
    search_agent
)

from shipment_manager import (
    create_shipment,
    view_shipments,
    search_shipment,
    assign_agent
)

from tracking_manager import (
    update_shipment_status,
    track_shipment
)

from report_manager import (
    shipment_statistics,
    pending_deliveries
)


def main():
    while True:
        print("\n" + "=" * 45)
        print("         COURIER TRACKING SYSTEM")
        print("=" * 45)

        print("1. Add Customer")
        print("2. View Customers")
        print("3. Search Customer")

        print("4. Add Delivery Agent")
        print("5. View Delivery Agents")
        print("6. Search Delivery Agent")

        print("7. Create Shipment")
        print("8. View Shipments")
        print("9. Search Shipment")
        print("10. Assign Delivery Agent")

        print("11. Update Shipment Status")
        print("12. Track Shipment")

        print("13. Shipment Statistics")
        print("14. Pending Deliveries")

        print("0. Exit")

        choice = input("\nEnter your choice: ").strip()

        actions = {
            "1": add_customer,
            "2": view_customers,
            "3": search_customer,
            "4": add_agent,
            "5": view_agents,
            "6": search_agent,
            "7": create_shipment,
            "8": view_shipments,
            "9": search_shipment,
            "10": assign_agent,
            "11": update_shipment_status,
            "12": track_shipment,
            "13": shipment_statistics,
            "14": pending_deliveries
        }

        if choice == "0":
            print("Thank you for using Courier Tracking System!")
            break

        action = actions.get(choice)

        if action:
            action()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
