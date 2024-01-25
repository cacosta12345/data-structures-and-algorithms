from data_structures.queue import Queue

class AnimalShelter:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue(self, animal):
        if isinstance(animal, Dog):
            self.dogs.enqueue(animal)
        elif isinstance(animal, Cat):
            self.cats.enqueue(animal)

    def dequeue(self, pref):
        if pref == "dog" and not self.dogs.is_empty():
            return self.dogs.dequeue()
        elif pref == "cat" and not self.cats.is_empty():
            return self.cats.dequeue()
        else:
            return None

class Dog:
    def __init__(self, name=""):
        self.species = "dog"
        self.name = name

class Cat:
    def __init__(self, name=""):
        self.species = "cat"
        self.name = name
