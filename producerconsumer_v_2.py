import random
from threading import Lock, Thread, Condition
from time import sleep

warehouse = []

max_elements = 10

warehouse_lock = Lock()

overflow_condition = Condition()

underflow_condition = Condition()

def is_overflow():
    return len(warehouse) >= max_elements

def is_underflow():
    return len(warehouse) == 0


def producer(id):
    while True:
        x = random.randint(a=1, b=10000)
        print('Thread {} produced number {}'.format(id, x))

        warehouse_lock.acquire()
        if not is_overflow():
            warehouse.append(x)
            warehouse_lock.release()
        else:
            with overflow_condition:
                warehouse_lock.release()
                print("Overflow. Producer {} waiting".format(id))
                overflow_condition.wait()

        with underflow_condition:
            underflow_condition.notify()
        sleep(random.random() * 5.0)


def consumer(id):
    while True:
        warehouse_lock.acquire()
        if not is_underflow():
            x = warehouse.pop(0)
            print('Thread {} consumed number {}'.format(id, x))
            warehouse_lock.release()
        else:
            with underflow_condition:
                warehouse_lock.release()
                print("Underflow. Consumer {} waiting".format(id))
                underflow_condition.wait()

        with overflow_condition:
            overflow_condition.notify()
        sleep(random.random() * 2.0)


for i in range(2):
    Thread(target=producer, args=(i, )).start()

for i in range(10):
    Thread(target=consumer, args=(i, )).start()

with overflow_condition:
    overflow_condition.notify_all()