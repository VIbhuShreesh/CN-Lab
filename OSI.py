# Define OSI Layers from top (Application) to bottom (Physical)
osi_layers = [
    "Application Layer",
    "Presentation Layer",
    "Session Layer",
    "Transport Layer",
    "Network Layer",
    "Data Link Layer",
    "Physical Layer"
]


# Sample data to send
def encapsulate_data(data):
    print("\nEncapsulation Process (Sender Side):")
    for layer in reversed(osi_layers):
        data = f"[{layer} Header] -> {data}"
        print(f"{layer}: {data}")
    return data


def decapsulate_data(data):
    print("\nDecapsulation Process (Receiver Side):")
    for layer in osi_layers:
        print(f"{layer}: {data}")
        start = data.find("->")
        if start != -1:
            data = data[start + 3:]  # Remove the current layer header
    return data


# Main simulation
if __name__ == "__main__":
    original_data = "Hello, Network!"
    print(f"Original Message: {original_data}")

    # Sender Side
    transmitted_data = encapsulate_data(original_data)

    # Receiver Side
    received_data = decapsulate_data(transmitted_data)

    print(f"\nReceived Message: {received_data}")
