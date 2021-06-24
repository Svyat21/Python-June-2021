import random
from asyncio import sleep, create_task, run, Lock

warehouse = []

max_elements = 10

warehouse_lock = Lock()


async def is_overflow():
    return len(warehouse) >= max_elements


async def is_underflow():
    return len(warehouse) == 0


async def producer(name):
    while True:
        x = random.randint(a=1, b=10000)

        await warehouse_lock.acquire()
        if not await is_overflow():
            warehouse.append(x)
            print(f'Produced_{name} added the number {x}')
            warehouse_lock.release()
        else:
            warehouse_lock.release()
            print(f'Overflow. Producer_{name} waiting...')
            while True:
                await sleep(0.1)
                if not warehouse_lock.locked():
                    break

        await sleep(random.random() * 5)


async def consumer(name):
    while True:
        await warehouse_lock.acquire()
        if not await is_underflow():
            x = warehouse.pop(0)
            print(f'Consumer_{name} took the number {x}')
            warehouse_lock.release()
        else:
            warehouse_lock.release()
            print(f'Underflow. Consumer {name} waiting...')
            while True:
                await sleep(0.1)
                if not warehouse_lock.locked():
                    break

        await sleep(random.random() * 5)


async def main():
    task1 = [create_task(producer(i)) for i in range(2)]
    task2 = [create_task(consumer(i)) for i in range(5)]
    for i in task1:
        await i
    for i in task2:
        await i


run(main())
