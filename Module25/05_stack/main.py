# TODO здесь писать код
                        # manager = TaskManager()
                        # manager.new_task("сделать уборку", 4)
                        # manager.new_task("помыть посуду", 4)
                        # manager.new_task("отдохнуть", 1)
                        # manager.new_task("поесть", 2)
                        # manager.new_task("сдать дз", 2)
                        # print(manager)
                        #
                        # Результат:
                        # 1 отдохнуть
                        # 2 поесть; сдать дз
                        # 4 сделать уборку; помыть посуду
class Stack:
    """Класс Stack представляющий собой список элементов, организованных по принципу LIFO"""

    def __init__(self):
        self.lst_task = []

    def add_task(self, task: str) -> None:
        """Метод add_task добавляет в список задачу"""
        self.lst_task.append(task)

    def delete_task(self, task: str) -> None:
        """Метод delete_task удаляет задачу из списка"""
        self.lst_task.remove(task)

    def __str__(self) -> str:
        """Метод __str__ выводит список задач"""
        return f'{', '.join(self.lst_task)}'


class TaskManager:
    """Класс TaskManager создает «Менеджер задач» в зависимости от приоритета задач"""

    def __init__(self, dct_task=None):
        if dct_task is None:
            dct_task = {}
        self.dct_task = dct_task

    def new_task(self, task: str, key: int) -> None:
        """Метод new_task добавляет в словарь задачи в зависимости от их приоритетов"""
        if not self.dct_task.get(key):
            self.dct_task[key] = Stack()
            self.dct_task.setdefault(key, []).add_task(task)
        else:
            if task in str(self.dct_task[key]):
                """При дублировании задачи ей присваивается приоритет ниже"""
                key += 1
                self.dct_task[key] = Stack()
            self.dct_task.setdefault(key, []).add_task(task)

    def remove_task(self, task: str) -> None:
        """Метод remove_task удаляет задачу из списка, при отсутствии выводит об этом сообщение,
        а так же если приоритет пуст(отсутствуют задачи) удаляет его"""
        for key, val in self.dct_task.items():
            if task in str(val):
                self.dct_task[key].delete_task(task)
                break
        else:
            print(f'Задачи - {task} в списке приоритетов нет')

        copy_dct = self.dct_task.copy()
        for key in copy_dct.keys():
            if len(str(copy_dct[key])) == 0:
                self.dct_task.pop(key)

    def __str__(self) -> str:
        """Метод __str__ выводит на консоль задачи в зависимости от приоритета"""
        return f'{'\n'.join(f'{key}: {val}'
                            for key, val in sorted(self.dct_task.items()))}'


manager = TaskManager()

# отсылаем задачу в пустой список
manager.remove_task("погулять с собакой")

# создаем словарь с задачами по приоритету
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать ДЗ", 2)
print(manager)
print()

# дублируем задачу с тем же приоритетом
manager.new_task("сделать уборку", 4)

# удаляем задачу
manager.remove_task("отдохнуть")
manager.remove_task("погулять")

print(manager)
