import random

class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= max(0, damage - self.defense)

    def attack_enemy(self, enemy):
        damage = random.randint(1, self.attack)
        enemy.take_damage(damage)
        print(f"{self.name} attacks {enemy.name} for {damage} damage.")

class Enemy(Character):
    pass

def main():
    player = Character("Player", 100, 20, 10)
    enemy = Enemy("Dragon", 200, 25, 5)

    print("Welcome to the Text-Based RPG!")
    print(f"You encounter a fearsome enemy: {enemy.name}")

    while player.is_alive() and enemy.is_alive():
        print(f"\n{player.name} (Health: {player.health}) vs {enemy.name} (Health: {enemy.health})")
        print("1. Attack")
        print("2. Run")

        choice = input("Enter your choice: ")

        if choice == '1':
            player.attack_enemy(enemy)
            if not enemy.is_alive():
                print(f"You defeated {enemy.name}!")
        elif choice == '2':
            print("You ran away!")
            break
        else:
            print("Invalid choice. Try again.")

        if enemy.is_alive():
            enemy.attack_enemy(player)
            if not player.is_alive():
                print("You were defeated. Game over.")

if __name__ == "__main__":
    main()
