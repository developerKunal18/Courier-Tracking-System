# Courier Tracking System

A Python-based Courier Tracking System designed to manage
customers, delivery agents, shipments, tracking updates,
and delivery reports.

## Features

- Customer Registration
- Delivery Agent Management
- Shipment Creation
- Unique Tracking ID Generation
- Delivery Agent Assignment
- Shipment Status Management
- Real-Time Local Tracking History
- Delivery Charge Calculation
- Shipment Search
- Delivery Statistics
- Pending Delivery Reports
- JSON Data Storage

## Technologies Used

- Python
- JSON
- Datetime
- UUID
- OS

## Project Structure

```text
courier-tracking-system/
├── main.py
├── config.py
├── storage.py
├── utils.py
├── customer_manager.py
├── agent_manager.py
├── shipment_manager.py
├── tracking_manager.py
├── report_manager.py
├── data/
│   ├── customers.json
│   ├── agents.json
│   └── shipments.json
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository.

```bash
git clone https://github.com/yourusername/courier-tracking-system.git
```

2. Open the project folder.

```bash
cd courier-tracking-system
```

3. Run the application.

```bash
python main.py
```

## How It Works

1. Register a customer.
2. Register a delivery agent.
3. Create a shipment.
4. Generate a unique tracking ID.
5. Assign a delivery agent.
6. Update the shipment status.
7. Track the shipment using its tracking ID.
8. Generate delivery reports.

## Shipment Status Flow

Booked
   |
Picked Up
   |
In Transit
   |
Out for Delivery
   |
Delivered

A shipment can also be cancelled before delivery.

## Delivery Charge Calculation

Delivery Charge = Base Charge + (Weight × Rate Per KG)

Example:

Base Charge = ₹50

Parcel Weight = 5 KG

Rate Per KG = ₹20

Total Delivery Charge = ₹150

## Sample Output

========== SHIPMENT TRACKING ==========

Tracking ID: TRK-A1B2C3D4

Receiver: Rahul Sharma

Destination: Mumbai

Current Status: In Transit

Tracking History:

2026-10-07 10:00:00 - Booked

2026-10-07 11:30:00 - Picked Up

2026-10-07 15:00:00 - In Transit

=======================================

## Future Improvements

- Flask Web Interface
- MySQL Database
- Login and Authentication
- QR Code Tracking
- SMS Notifications
- Email Notifications
- PDF Shipping Labels
- REST API
- Delivery Dashboard

## Author

Kunal Karbhari

GitHub: https://github.com/developerKunal18

## Challenge

365 Days of Python Projects

Day 350 Completed
