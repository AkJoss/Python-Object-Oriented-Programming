# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:33:15 2024

@author: José Alberto Rocha Munguía
"""

# Turn-based Pokemon battle (OOP): choose two Pokemon and fight.
# Run:
#   python3 pokemon_battle.py
#
# Flow:
#   1) Pick your Pokemon by number (1-4)
#   2) Pick the opponent by number (different one)
#   3) Each turn: type an attack name EXACTLY as shown, or "defend"
#   4) Opponent picks at random. Fight until one reaches 0 HP.
#
# Type chart used here: Fire > Grass > Water > Fire
# Super effective = 1.5x damage | not very effective = 0.5x
# "defend" halves damage on the next hit (and skips your attack that turn if you defend).

import random

class Pokemon:
    def __init__(self, name, pokemon_type, hp, attacks):
        self.name = name
        self.pokemon_type = pokemon_type
        self.hp = hp
        self.attacks = attacks
        self.defense_active = False

    def attack(self, attack_name, opponent):
        if self.defense_active:
            print(f"{self.name} cannot attack while defending.")
            self.defense_active = False  # Reset defense after turn
            return

        # Damage calculation considering types
        base_damage = self.attacks[attack_name]
        multiplier = 1

        # Type effectiveness logic
        if (self.pokemon_type == "Fire" and opponent.pokemon_type == "Grass") or \
           (self.pokemon_type == "Grass" and opponent.pokemon_type == "Water") or \
           (self.pokemon_type == "Water" and opponent.pokemon_type == "Fire"):
                multiplier = 1.5
                print("It's super effective!")
        elif (self.pokemon_type == "Fire" and opponent.pokemon_type == "Water") or \
             (self.pokemon_type == "Grass" and opponent.pokemon_type == "Fire") or \
             (self.pokemon_type == "Water" and opponent.pokemon_type == "Grass"):
                multiplier = 0.5
                print("It's not very effective...")

        final_damage = int(base_damage * multiplier)
        print(f"{self.name} uses {attack_name} and deals {final_damage} damage to {opponent.name}.")
        opponent.receive_damage(final_damage)

    def receive_damage(self, damage):
        if self.defense_active:
            damage //= 2  # Reduces damage by half
            print(f"{self.name} defended part of the attack.")
            self.defense_active = False  # Reset defense

        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} now has {self.hp} HP.")

    def defend(self):
        self.defense_active = True
        print(f"{self.name} is in a defensive stance.")

    def is_alive(self):
        return self.hp > 0

############################################################################

class PokemonBattle:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def show_status(self):
        print("\nBattle Status:")
        print(f"{self.pokemon1.name} - HP: {self.pokemon1.hp}")
        print(f"{self.pokemon2.name} - HP: {self.pokemon2.hp}")

    def execute_turn(self, pokemon, action, opponent):
        if action in pokemon.attacks:
            pokemon.attack(action, opponent)
        elif action == "defend":
            pokemon.defend()
        else:
            print("Invalid action. Try again.")

############################################################################
if __name__ == "__main__":
    # Roster — change HP / attack power here if you want a shorter fight
    pokemon_list = [
        Pokemon("Riolu", "Fighting", 100, {"Bullet Punch": 20, "Aura Sphere": 40}),
        Pokemon("Charmander", "Fire", 120, {"Flamethrower": 18, "Fire Blast": 24}),
        Pokemon("Squirtle", "Water", 100, {"Water Gun": 16, "Hydro Pump": 26}),
        Pokemon("Bulbasaur", "Grass", 100, {"Vine Whip": 15, "Solar Beam": 25}),
    ]

    print("Choose your Pokemon:")
    for i, p in enumerate(pokemon_list):
        print(f"{i + 1}. {p.name} - Type: {p.pokemon_type} - HP: {p.hp}")

    player_choice = int(input("Pokemon number: ")) - 1
    player = pokemon_list[player_choice]

    print("\nChoose the opponent Pokemon:")
    for i, p in enumerate(pokemon_list):
        if i != player_choice:
            print(f"{i + 1}. {p.name} - Type: {p.pokemon_type} - HP: {p.hp}")

    opponent_choice = int(input("Opponent number: ")) - 1
    opponent = pokemon_list[opponent_choice]

    battle = PokemonBattle(player, opponent)

    while player.is_alive() and opponent.is_alive():
        battle.show_status()
        actions = list(player.attacks.keys()) + ["defend"]
        print(f"\n{player.name}'s turn. Choose an action: {actions}")
        player_action = input("Type your choice: ")

        opponent_action = random.choice(list(opponent.attacks.keys()) + ["defend"])

        battle.execute_turn(player, player_action, opponent)

        if opponent.is_alive():
            battle.execute_turn(opponent, opponent_action, player)

    if player.is_alive():
        print(f"\n{player.name} has won the battle!")
    else:
        print(f"\n{opponent.name} has won the battle!")
