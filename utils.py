import uuid
from datetime import datetime


def generate_id(prefix):
    return f"{prefix}-{uuid.uuid4().hex[:8].upper()}"


def current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def find_by_id(records, record_id, key="id"):
    return next(
        (record for record in records
         if record.get(key) == record_id),
        None
    )


def calculate_delivery_charge(weight):
    from config import (
        BASE_DELIVERY_CHARGE,
        CHARGE_PER_KG
    )

    return round(
        BASE_DELIVERY_CHARGE + weight * CHARGE_PER_KG,
        2
    )
