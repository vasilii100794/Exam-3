#Task_3
# Класс Company
# 1. Создайте класс Company
# 2. Создайте статистическое свойство levels, которое будет содержать (как словарь) все уровни квалификации
#    программиста: 1:junior , 2:middle, 3:senior,4:lead
# 3. Создайте метод _init_, внутри которого будет определены два protected свойства:
#    1._index - передается параметром 2._levels - принимает из словаря levels значения с ключом _index
# 4. Создайте метод _level_up(), который будет переводить программиста на следующий уровень
# 5. Создайте метод is_lead(), который будет проверять, что программист достиг последней квалификации
# Класс Programmer:
# 1. Создайте класс Programmer
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства:
#    1) name - передается параметром, является публичным
#    2) age - возраст
#    3)level – уровень квалификации на основе словаря из Company
# 3. Создайте метод work(), который заставляет программиста работать, что позволяет ему становиться более
#    квалифицированным с помощью метода _level_up()
# 4. Создайте метод info(), который выведет информацию о вас: имя, возраст, квалификацию
# 5. Создайте статический метод knowledge_base(), который выведет в консоль справку по программированию (просто
#    любой текст).
class Company:
    levels = {1: "junior", 2: "middle", 3: "senior", 4: "lead"}
    def __init__(self, index):
        if index > 4:
            index = 4
        self._index = index
        self._levels = self.levels[self._index]
        print(f"Ваш уровень: {self._levels}")
    def _level_up(self):
        if self._index != 4:
            self._index += 1
            self._levels = self.levels[self._index]
        print(f'Вы подняли свой уровень до: {self._levels}')
    def is_lead(self):
        if self._index == 4:
            print('Вы достигли максимального уровня!')
        else:
            print(f'Ваш уровень квалификации: {self.levels[self._index]}. Необходимо поднять уровень!')
            return self._index == 4

class Programmer(Company):
    def __init__(self, name, age, level):
        super().__init__(level)
        self.name = name
        self.age = age
    def work(self):
        self._level_up()
    def info(self):
        print(self.name, self.age, self._levels)
    @staticmethod
    def knowledge_base():
        print("Вы досигли цели!")

print('Проверка по классу Company:')
obj_1 = Company(1)
obj_1._level_up()
obj_1.is_lead()
print()
print('Проверка по дочернему классу Programmer:')
obj_2 = Programmer('Василий', 28, 1)
obj_2.info()
while obj_2.is_lead() == False:
    obj_2.work()
obj_2.info()
obj_2.knowledge_base()
