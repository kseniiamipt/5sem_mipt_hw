1) Чем классовая переменная отличается от поля? В какой ситуации можно через поле влиять на поля других экземпляров?
Каждый экземпляр будет иметь одинаковое значение данной переменной класса, переменные класса одни и те же для всех экземпляров. Поле же у каждого экземпляра принимает свои значения. Для того, чтобы можно было через поле влиять на поля других экземпляров нужно классовую переменную сделать изменяемым объектом
например, так:
class A:
    s = [1, 2]

a = A()
b = A()

print(a.s, b.s)

b.s.append(3)
print(a.s, b.s)

вывод
[1, 2] [1, 2]
[1, 2, 3] [1, 2, 3]

2) Как называется типизация в питоне и какой идеей она руководствуется?
Утиная типизация. Если что-то выглядит как утка, плавает как утка и крякает как утка, это наверняка и есть утка. Функция делает определенное действие, с подаваемыми на вход объектами, например, складывает. Если функция может сделать это с текущими объектами, то она сделает это. И ей все равно на тип данных. То есть одна и та же функция может использоваться и для типа целых чисел, вещественных, можем складывать целые и вещественные и ошибки не будет, в то время как в других языках может возникнуть перегрузка.
3) Каким образом мы реализуем полиморфизм для созданных нами объектов?
Мы переопрделяем методы для класса. То есть какие-то встроенные опереции сложения и пт теперь могут работать по-другому, так как мы захотели
4) Зачем переопределять метод _radd_() наравне с _add_()?
операция x + y будет сначала пытаться вызвать x.__add__(y), если это не получилось, будет пытаться вызвать y.__radd__(x). Это имеет смысл прописывать, когда мы работаем с разными классами.