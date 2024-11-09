class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        raise NotImplementedError

    def info(self):
        print(f"Это {self.__class__.__name__}. Имя: {self.name}, Возраст: {self.age} лет.")


class Dog(Animal):
    def speak(self):
        print("Гав-гав")

    def fetch(self):
        print(f"{self.name} приносит палку!")


class Cat(Animal):
    def speak(self):
        print("Мяу-мяу")

    def climb(self):
        print(f"{self.name} карабкается на дерево!")


class Bird(Animal):
    def speak(self):
        print("Чик-чирик")

    def fly(self):
        print(f"{self.name} летает высоко в небе!")


dog = Dog(name="Пальма", age=3)
cat = Cat(name="Киндер", age=2)
bird = Bird(name="Арчи", age=1)


for animal in (dog, cat, bird):
    animal.info()
    animal.speak()

dog.fetch()
cat.climb()
bird.fly()
