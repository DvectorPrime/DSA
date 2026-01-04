import random
class Character:
    def __init__(self, name, hp, attack_power):
        self._name = name
        self._hp = hp
        self.max_hp = hp
        self.attack_power = attack_power

    @property
    def hp(self):
        return self._hp

    def take_damage(self, damage):
        self._hp -= damage
        if self._hp <= 0: 
            self._hp = 0

    def is_alive(self):
        return self._hp > 0

    def attack(self, target):
        raise NotImplementedError("Subclass must implement abstract method")

class Warrior(Character):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)
        self.rage = 0

    def attack(self, target):
        damage = self.attack_power
        target.take_damage(damage)
        self.rage += 10
        print(f"And {self._name} rage")

class Mage(Character):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)
        self.mana = 100

    def attack(self, target):
        damage = 0
        if self.mana >= 20:
            damage = random.randrange(10, self.attack_power)
            target.take_damage(damage)
            self.mana -= 20
        else:
            damage = random.randrange(0, 10)
            target.take_damage(damage)

        print(f"{self._name} has done {damage} damage")

def run_battle(hero, enemy):
    print(f"--- Battle Start: {hero._name} VS {enemy._name} ---")
    
    hero_turn = True
    while hero.is_alive() and enemy.is_alive():
        if hero_turn:
            hero.attack(enemy)
            print(f"{enemy._name} has {enemy.hp} HP")
        else:
            enemy.attack(hero)
            print(f"{hero._name} has {hero.hp} HP")

        hero_turn = not hero_turn

    if hero.is_alive():
        print(f"{hero._name} wins! {enemy._name} loses")
    else:
        print(f"{enemy._name} wins! {hero._name} loses")

aragorn = Warrior("Aragorn", 100, 10)
gandalf = Mage("Gandalf", 60, 30)
run_battle(aragorn, gandalf)