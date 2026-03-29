import threading

import time

def my_function(name):
    for i in range(3):
        print(f"Thread {name} is running...")
        time.sleep(1)

# Create threads
t1 = threading.Thread(target=my_function, args=("1",))
t2 = threading.Thread(target=my_function, args=("2",))

# Start threads
t1.start()
t2.start()

# Wait for both threads to complete
t1.join()
t2.join()