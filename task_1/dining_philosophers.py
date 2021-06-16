from threading import Thread, Lock
from time import sleep
from random import random

forks = [Lock() for _ in range(5)]


def philosopher(name):
    amount_of_forks = []
    required_quantity = 2
    while True:
        for fork in forks:
            if len(amount_of_forks) == required_quantity:
                print(f'Философ {name} - обедает!')
                sleep(random() * 3)
                amount_of_forks = [f.release() for f in amount_of_forks]
                amount_of_forks.clear()
                print(f'Философ {name} - обедать закончил!')
                sleep(random() * 3)
                break
            elif not fork.locked():
                fork.acquire()
                amount_of_forks.append(fork)
        else:
            print(f'У философа {name} - {len(amount_of_forks)} вилок, он ожидает очереди.')
            sleep(0.1)


for i in range(5):
    thread = Thread(target=philosopher, args=(i,))
    thread.start()
