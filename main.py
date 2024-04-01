'''
2. Напишите класс Python, который имеет два метода get_String и print_String.
get_String принимает строку от пользователя и print_String печатает строку в верхнем регистре.
'''
# class Python:
#     def __init__(self) -> None:
#         pass
#     def get_string(self, user_text):
#         self.user_text = input('Введите свой текст: ')
#     def print_string(self):
#         capslock = self.user_text.upper()
#         print(capslock)

# data = Python()
# data.get_string('sdsd') # Введите текст
# data.print_string() # печатать текст пользователя в верхнем регистре

'''
4. Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и age.
По умолчанию name = Ivan, age = 18, groupNumber = 10A. Необходимо создать пять методов:
getName, getAge, getGroupNumber, setNameAge, setGroupNumber. Метод getName нужен для получения данных
об имени конкретного студента, метод getAge нужен для получения данных о возрасте конкретного студента,
vетод setGroupNumberнужен для получения данных о номере группы конкретного студента.
Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию, метод setGroupNumber
позволяет изменить номер группы установленный по умолчанию. В программе необходимо создать пять экземпляров класса Student,
установить им разные имена, возраст и номер группы.
'''

class Student:
    def __init__(self, name, groupNumber, age) -> None:
        self.name = 'Эмир'
        self.groupNumber = 15
        self.age = 30
class GetName(Student):
    print(f'Имя пользователя: {self.name}')