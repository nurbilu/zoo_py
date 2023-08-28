from enum import Enum
import json

class ZooActions(Enum):
  PRINT = 0
  PRINT_PREDATORS = 1
  PRINT_PREY = 2
  ADD = 3
  DELETE = 4
  SEARCH = 5
  EXIT = 9

class Animals:
  def __init__(self, name, category):
    self.name = name
    self.category = category

  def get_details(self):
    return f"{self.name} ({self.category})"

class Lion(Animals):
  def __init__(self, name):
    super().__init__(name, "Predator")

  def roar(self):
    print(f"{self.name} roars loudly!")
    
class Zebra(Animals):
  def __init__(self, name):
    super().__init__(name, "Prey")

  def graze(self):
    print(f"{self.name} grazes on grass.")

class ZooManager(Animals):
  def __init__(self):
    self.animals = {}
    self.load_animals()

  def load_animals(self):
    try:
      with open("animals.json") as f:
        self.animals = json.load(f)
        
        # Add Lion and Zebra classes
        for name, data in self.animals.items():
          if data['category'] == 'Predator':
            self.animals[name] = Lion(name)
          elif data['category'] == 'Prey':
            self.animals[name] = Zebra(name)
            
    except FileNotFoundError:
      print("No animal data file found, starting with empty zoo")

  def save_animals(self):
    with open("animals.json", "w") as f:
      json.dump(self.animals, f)
    print("Animals data saved to file")

  def print_animals(self):
    print("Animals:")
    for animal in self.animals.values():
      print(animal.get_details())

  def print_predators(self):
    print("Predators:")
    for animal in self.animals.values():
      if animal.category == "Predator":
        print(animal.name)

  def print_prey(self):
    print("Prey:")
    for animal in self.animals.values():
      if animal.category == "Prey":
        print(animal.name)

  def add_animal(self, name, category):
    if category == "predator":
      animal = Lion(name)
    elif category == "prey":
      animal = Zebra(name)
    else:
      print("Invalid category")
      return

    self.animals[name] = animal
    print(f"{name} added to zoo as a {category}")

  def delete_animal(self, name):
    if name in self.animals:
      del self.animals[name]
      print(f"{name} removed from zoo")
    else:
      print(f"{name} not found in zoo")

  def search_animal(self, name):
    if name in self.animals:
      print(self.animals[name].get_details())
    else:
      print(f"{name} not found in zoo")

def menu():
  zoo = ZooManager()

  while True:
    print()
    print("Menu:")
    print(f"{ZooActions.PRINT.value} - Print all animals")
    print(f"{ZooActions.PRINT_PREDATORS.value} - Print predators")
    print(f"{ZooActions.PRINT_PREY.value} - Print prey")
    print(f"{ZooActions.ADD.value} - Add animal")
    print(f"{ZooActions.DELETE.value} - Delete animal")
    print(f"{ZooActions.SEARCH.value} - Search for animal")
    print(f"{ZooActions.EXIT.value} - Exit")

    choice = int(input("Enter choice: "))

    if choice == ZooActions.PRINT.value:
      zoo.print_animals()
    elif choice == ZooActions.PRINT_PREDATORS.value:
      zoo.print_predators()
    elif choice == ZooActions.PRINT_PREY.value:
      zoo.print_prey()
    elif choice == ZooActions.ADD.value:
      name = input("Enter name: ")
      category = input("Enter category (predator/prey): ")
      zoo.add_animal(name, category)
    elif choice == ZooActions.DELETE.value:
      name = input("Enter name to delete: ")
      zoo.delete_animal(name)
    elif choice == ZooActions.SEARCH.value:
      name = input("Enter name to search: ")
      zoo.search_animal(name)
    elif choice == ZooActions.EXIT.value:
      zoo.save_animals()
      print("Exiting...")
      break
    else:
      print("Invalid choice")

if __name__ == "__main__":
  menu()