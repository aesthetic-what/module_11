from queue import Queue
from threading import Thread
from random import randint
import time

class Table():
    def __init__(self, number: int):
        self.number = number
        self.guest = None

class Guest(Thread):
    queue = Queue()
    def __init__(self, name: str):
        super().__init__()
        self.name = name
    
    def run(self):
        time.sleep(randint(3, 10))

class Cafe():
    def __init__(self, *tables):
        self.tables = list(tables)
        self.queue = Queue()
    
    def guest_arrival(self, *guests):
        for guest in guests:
            if any(table.guest is None for table in self.tables):
                for table in self. tables:
                    if table.guest is None:
                        table.guest = guest
                        guest.start()
                        print(f'{guest.name} сел(-а) за стол номер {table.number}')
                        break
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')


    def discuss_guest(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)\nСтол номер {table.number} свободен")
                    table.guest = None
                    break

            if self.queue and any(table.guest is None for table in self.tables):
                for table in self.tables:
                    if table.guest is None:
                        guest = self.queue.get()
                        table.guest = guest
                        guest.start()
                        print(f"{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                        break
# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guest()