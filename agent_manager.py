from config import AGENT_FILE
from storage import load_data, save_data
from utils import generate_id, find_by_id


def add_agent():
    agents = load_data(AGENT_FILE)

    name = input("Agent Name: ").strip()
    phone = input("Phone Number: ").strip()
    area = input("Delivery Area: ").strip()

    if not all([name, phone, area]):
        print("All fields are required.")
        return

    agent = {
        "id": generate_id("AGT"),
        "name": name,
        "phone": phone,
        "area": area
    }

    agents.append(agent)
    save_data(AGENT_FILE, agents)

    print("Delivery agent added successfully!")
    print("Agent ID:", agent["id"])


def view_agents():
    agents = load_data(AGENT_FILE)

    if not agents:
        print("No delivery agents found.")
        return

    for agent in agents:
        print("-" * 40)
        print("ID:", agent["id"])
        print("Name:", agent["name"])
        print("Phone:", agent["phone"])
        print("Area:", agent["area"])


def search_agent():
    agent_id = input("Enter Agent ID: ").strip()

    agents = load_data(AGENT_FILE)
    agent = find_by_id(agents, agent_id)

    if agent:
        for key, value in agent.items():
            print(f"{key}: {value}")
    else:
        print("Agent not found.")
