""" An object is a container for variables and functions

    for example, a monster object might contain:
    Variables for health, energy, stamina, damage
    Functions for attack, movement, animations

    although, they have special names
    Variables in an object are called attributs
    Functions in an object are called methods"""

class Monster1:
    # attributes
    health = 90
    energy = 20

    # methods
    def attack(self):
        print("Monster 1 attack")
    def block(self):
        print("Monster 1 block")

class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
    def attack(self, amount):
        print("Monster attack")
        print(f"{amount} damage was dealt")
        self.energy -= 20
        print(f"{self.energy} energy was consumed")
    def block(self):
        print("Monster block")
    def move(self, speed):
        print(f"The speed of the monster is {speed}")
    def get_damage(self, amount):
        self.health -= amount
        print(f"Health after damage is {self.health}")
monster2 = Monster(70, 40)
monster1 = Monster(40, 60)
monster3 = Monster(health = 100, energy = 30)
print(f"Monster 3 health is {monster3.health} and energy is {monster3.energy}")
monster2.block()
print(monster1.energy, monster1.health)

monster2.attack(30)
print(monster2.energy)
monster2.move(50)


class Hero:
    def __init__(self, damage, monster):
        self.monster = monster
        self.damage = damage
    def attack(self):
        self.monster.get_damage(self.damage)

hero = Hero(30, monster2)
hero.attack()
print(monster2.health)

class Scorpian(Monster):
    def __init__(self, poison_damage, scorpian_health, scorpian_energy):
        self.poison_damage = poison_damage
        super().__init__(health = scorpian_health, energy = scorpian_energy)
    def attack(self):
        print("The scorpian has attacked")
        print(f"It has dealt {self.poison_damage} poison damage")
scorpian = Scorpian(50, 10, 10)
scorpian.attack()

class Fish:
    def __init__(self,speed, has_scales):
        self.speed = speed
        self.has_scales = has_scales
    def swim(self):
        print(f"The fish is swimming at a speed of {self.speed}")
class Shark(Monster, Fish):
    def __init__(self, bite_strength, health, energy, speed, has_scales):
        self.bite_strength = bite_strength
        super().__init__(health, energy)  # Call Monster's __init__ method
        super().__init__(speed, has_scales)

shark = Shark(30, health = 30, energy= 30, has_scales=True, speed=40)
print(Shark.mro())






