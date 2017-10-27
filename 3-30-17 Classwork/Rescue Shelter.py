import time

class Animal:
    num_animals = 0
    def __init__(self, name, type, arrival_date=time.strftime("%d/%m/%y"), adoption_date="No adoption date yet"):
        Animal.num_animals += 1
        self.id = Animal.num_animals
        self.name = name
        self.type = type
        self.arrival_date = arrival_date
        self.adoption_date = adoption_date

    def setAdoptionDate(self, adoption_date):
        self.adoption_date = adoption_date
