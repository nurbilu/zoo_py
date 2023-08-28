# Lion class represents an animal with a name, species, and age.
class Lion:
    # Constructor to initialize an Lion object.
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.energy = 100  # Initial energy level (assuming it's a value between 0 and 100)
        
    def __str__(self) -> str:
        return f"{self.name}'s energy level: {self.get_energy()}"


    # Simulate the animal eating and replenishing energy.
    def eat(self, food):
        print(f"{self.name} is eating {food}")
        self.energy += 20  # Increase energy by 20 units when eating

    # Simulate the animal sleeping and gaining energy.
    def sleep(self, hours):
        print(f"{self.name} is sleeping for {hours} hours")
        self.energy += hours * 10  # Increase energy based on the hours of sleep

    # Make the animal produce a sound.
    def make_sound(self, sound):
        print(f"{self.name} makes a {sound} sound")

    # Get the current energy level of the animal.
    def get_energy(self):
        return self.energy

# Example usage:
if __name__ == "__main__":
    lion = Lion("Alex", "Lion", 5)
    lion.make_sound("Roar")
    lion.eat("meat")
    lion.sleep(8)
    
    print(lion)
