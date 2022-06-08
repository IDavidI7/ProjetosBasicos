import time
from threading import Thread
import wget


def suatia(t, msg):
    for i in range(10):
        time.sleep(t)
        print(msg)

t1 = Thread(target=suatia, args=(1,'oi sou a t1'))
t2 = Thread(target=suatia, args=(1.5, 'oi sou a t2'))
t1.start()
t2.start()
while True:
    print('Leu me deu')
    time.sleep(.5)
