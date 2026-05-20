active_devices = {}

def register_device(device_id, location):

    active_devices[device_id] = {
        "location": location,
        "status": "ACTIVE"
    }

def fetch_device(device_id):

    return active_devices.get(device_id)
