from enum import Enum
import json


class Zoo_Actions(Enum):
    PRINT = 0
    PRINT_PREDATORS = 2
    PRINT_PRAY = 3
    ADD = 4
    DELETE = 5
    SEARCH = 6
    EXIT = 9


class ZooManager:
    def __init__(self):
        with open('zoo_data.json') as f:
            data = json.load(f)
            self.animals = data

    def print_animals(self):
        print("Animals in the zoo:")
        for animal, category in self.animals.items():
            print(f"{animal}: {category}")

    def print_predators(self):
        print("Predator animals:")
        for animal, category in self.animals.items():
            if category == 'Predator':
                print(animal)

    def print_prey(self):
        print("Prey animals:")
        for animal, category in self.animals.items():
            if category == 'Prey':
                print(animal)

    def add_animal(self, name, category):
    # Convert abbreviated category input to full category names
        if category.lower() == "pred":
            full_category = "Predator"
        elif category.lower() == "pre":
            full_category = "Prey"
        else:
            print("Invalid category input. Please use 'Pred' for Predator or 'Pre' for Prey.")
            return

        self.animals[name] = full_category
        print(f"{name} has been added to the zoo as a {full_category}.")


    def delete_animal(self, name):
        if name in self.animals:
            del self.animals[name]
            print(f"{name} has been removed from the zoo.")
        else:
            print(f"{name} is not in the zoo.")

    def search_animal(self, name):
        if name in self.animals:
            print(f"{name} is in the zoo and is a {self.animals[name]}.")
        else:
            print(f"{name} is not in the zoo.")
    def load_zoo(self):
        try:
            with open("zoo_data.json", "r") as file:
                self.animals = json.load(file)
        except FileNotFoundError:
            print("No saved zoo data found. Starting with an empty zoo.")

    def save_zoo(self):
        with open("zoo_data.json", "w") as file:
            json.dump(self.animals, file)
        print("Zoo data saved successfully.")
    
    def print_menu():
        pass
#     print("\nZoo Management Menu:")
#     for action in Zoo_Actions:
#         print(f"{action.value}. {action.name.replace('_', ' ').title()}")
#     print(f"Enter your choice ({', '.join([str(action.value) for action in Zoo_Actions])}): ", end="")

def menu():
    zoo_manager = ZooManager()
    # print_menu()
    while True:
        print("\nZoo Management Menu:\n")
        print(f"{Zoo_Actions.PRINT.value}. Print all animals")
        print(f"{Zoo_Actions.PRINT_PREDATORS.value}. Print predators")
        print(f"{Zoo_Actions.PRINT_PRAY.value}. Print prey")
        print(f"{Zoo_Actions.ADD.value}. Add an animal")
        print(f"{Zoo_Actions.DELETE.value}. Delete an animal")
        print(f"{Zoo_Actions.SEARCH.value}. Search for an animal")
        print(f"{Zoo_Actions.EXIT.value}. Exit")
        
        choice = int(input("\nEnter your choice: "))
        
        if choice == Zoo_Actions.PRINT.value:
            zoo_manager.print_animals()
        elif choice == Zoo_Actions.PRINT_PREDATORS.value:
            zoo_manager.print_predators()
        elif choice == Zoo_Actions.PRINT_PRAY.value:
            zoo_manager.print_prey()
        elif choice == Zoo_Actions.ADD.value:
            name = input("Enter the name of the animal to add: ")
            category = input("Enter the category (Pred or Pre): ")
            zoo_manager.add_animal(name, category)
        elif choice == Zoo_Actions.DELETE.value:
            name = input("Enter the name of the animal to delete: ")
            zoo_manager.delete_animal(name)
        elif choice == Zoo_Actions.SEARCH.value:
            name = input("Enter the name of the animal to search: ")
            zoo_manager.search_animal(name)
        elif choice == Zoo_Actions.EXIT.value:
            zoo_manager.save_zoo()  # Save zoo data before exiting
            print("Exiting the zoo management system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
