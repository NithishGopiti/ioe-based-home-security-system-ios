synchronized_devices = {}

def synchronize_device(device_id):

    synchronized_devices[device_id] = "SYNCED"

    return {
        "device_id": device_id,
        "status": "SYNCED"
    }
