#Создайте класс Tomato
class Tomato:

    #Создайте статическое свойство states, которое будет содержать все стадии созревания помидора
    states = {0:'Ничего',1:'Росток', 2:'Цветок', 3:'Зелёный помидор', 4:'Красный помидор'}

    #Создайте метод __init__(), внутри которого будут определены два динамических protected свойства:
    # 1) _index - передается параметром и 2) _state- принимает первоезначение из словаря states
    def __init__(self, index):
        self._index = index
        self._state = 0

    #Создайте метод grow(), который будет переводить томат наследующую стадию созревания
    def grow(self):
        self._change_state()

    #Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг последней стадии созревания)
    def is_ripe(self):
        if self._state == 4:
            return True
        else:
            return False

    #Метод который проверяет на какой стадии находится помидор
    def _change_state(self):
        if self._state < 4:
            self._state += 1
        else:
           self._print_state()
    #Метод выводит стадию помидора
    def _print_state(self):
        print(f'Стадия помидора {self._index} - {Tomato.states[self._state]}')

#Создайте класс TomatoBush
class TomatoBush:

    #Определите метод __init__(), который будет принимать в качестве параметра количество томатов и на его основе будет
    #создавать список объектов класса Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    #Создайте метод grow_all(), который будет переводить все объекты из списка томатов на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    #Создайте метод all_are_ripe(), который будет возвращать True,если все томаты из списка стали спелыми
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    #Создайте метод give_away_all(), который будет чистить список томатов после сбора урожая
    def give_away_all(self):
        self.tomatoes = []

class Gardener:

    #Создайте метод __init__(), внутри которого будут определены два динамических свойства: 1) name - передается параметром
    #, является публичным и 2) _plant - принимает объект класса Tomato, является protected
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    #Создайте метод work(), который заставляет садовника работать,что позволяет растению становиться более зрелым
    def work(self):
        print('Садовник работает')
        self._plant.grow_all()
        print('Садовник закончил')

    #Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все - садовник собирает урожай.
    #Если нет - метод печатает предупреждение.
    def harvest(self):
        print('Садовник собирает урожай')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Сборка урожая завершена')
        else:
            print('Слишком рано. Растение еще не созрело')

    #Создайте статический метод knowledge_base(), который выведет в консоль справку по садоводству.
    @staticmethod
    def knowledge_base():
        print('Помидоры, пожалуй, один из самых любимых овощей у дачников. Но в условиях короткого прохладного лета томаты'
              ' могут капризничать и не давать полноценных урожаев. Поэтому важно обеспечить им комфортные условия.')

if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Борис', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()