import json
import os


def load_data(filename):
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_data(filename, data):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
