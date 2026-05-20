import queue
import threading

event_queue = queue.Queue()

def producer(events):

    for event in events:
        event_queue.put(event)

def consumer():

    while not event_queue.empty():

        event = event_queue.get()

        print(
            f"Processing event {event['sensor_id']}"
        )

def start_processing(events):

    producer_thread = threading.Thread(
        target=producer,
        args=(events,)
    )

    consumer_thread = threading.Thread(
        target=consumer
    )

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()
