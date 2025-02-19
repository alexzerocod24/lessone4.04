class Bird():
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color

    def fly(self):
        print(f"{self.name} летает")

    def eat(self):
        print(f"{self.name} летает")

    def sing(self):
        print(f"{self.name} поёт - чирик")

    def info(self):
        print(f"{self.name} - имя")
        print(f"{self.voice} - голос")
        print(f"{self.color} - окрас птицы")


class Pigeon(Bird):
    def __init__(self, name, voice, color, favorite_food):
        super().__init__( name, voice, color)
        self.favorite_food = favorite_food

    def sing(self):
        print(f"{self.name} - поёт курлык-курлык")

    def walk(self):
        print(f"{self.name} - гуляет")

bird = Pigeon("Гоша", "курлык", "серый", "хлебные крошки")



bird.sing()
bird.info()
bird.walk()