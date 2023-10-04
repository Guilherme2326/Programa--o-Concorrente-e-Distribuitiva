import colorama
import time 
from threading import Thread
from queue import Queue
from colorama import init, Fore, Back, Style
init(convert=True)

def gera_dados(queue):
    while queue.qsize() > 0:
        valor = queue.get()
        print(colorama.Fore.RED + f'Dado {valor*2} Processado. ', flush=True)
        time.sleep(1)
        queue.task_done()

def consome_dados(queue):
    while queue.qsize() > 0:
        valor = queue.get()
        print(f'Dado {valor*2} Processado. ', flush=True)
        time.sleep(1)
        queue.task_done()

if __name__ == '__main__':
    print('Sistema iniciado', flush=True)
    queue = Queue()
    t1 = Thread(target=gera_dados,args=(queue,))
    t2 = Thread(target=consome_dados, args=(queue,))

    t1.start()
    t1.join()

    t2.start()
    t2.join() 