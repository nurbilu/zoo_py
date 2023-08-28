class Fish:
    # Constructor to initialize a Fish object.
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.energy = 100  # Initial energy level (assuming it's a value between 0 and 100)

    def __str__(self) -> str:
        return f"{self.name}'s energy level: {self.get_energy()}"

    # Simulate the fish eating and replenishing energy.
    def eat(self, food):
        print(f"{self.name} is eating {food}")
        self.energy += 15  # Increase energy by 15 units when eating

    # Simulate the fish swimming and using energy.
    def swim(self, distance):
        print(f"{self.name} is swimming for {distance} meters")
        self.energy -= distance * 2  # Decrease energy based on the distance swum

    # Make the fish produce a sound (e.g., bubbles).
    def make_sound(self, sound):
        print(f"{self.name} makes a {sound} sound")

    # Get the current energy level of the fish.
    def get_energy(self):
        return self.energy

# Example usage:
if __name__ == "__main__":
    fish = Fish("Nemo", "Clownfish", 2)
    fish.make_sound("Bubble")
    fish.eat("plankton")
    fish.swim(10)
    
    print(fish)
