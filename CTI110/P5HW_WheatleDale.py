# Main function to organize gameplay

import random  # Importing a library for generating random events

# Function that returns a game character as a dictionary
def get_character():
    return {"name": "Mario", "health": 100, "coins": 0}

# Function to calculate damage taken
def calculate_damage(player, enemy_damage):
    player["health"] -= enemy_damage
    return player

# Function to collect coins by jumping
def jump_and_collect_coins(player):
    coins_collected = random.randint(1, 10)  # Randomly generates the number of coins Mario collects by jumping
    player["coins"] += coins_collected
    print(f"Mario jumped and collected {coins_collected} coins!")
    return player

# Function to determine enemy based on user input
def encounter_enemy(direction):
    if direction == "left":
        enemy = "Goomba"
        damage = random.randint(5, 15)
    elif direction == "right":
        enemy = "Koopa"
        damage = random.randint(10, 20)
    else:
        print("Invalid input! Mario stumbled and avoided the enemy.")
        enemy, damage = None, 0
    return enemy, damage

# Main function to organize gameplay
def main():
    mario = get_character()
    
    print("\nWelcome to Mario's Adventure!")
    print("Choose 'left' or 'right' to decide Mario's path, or type 'jump' to collect coins.\n")
    
    while True:  # Loop until Mario's health is depleted
        action = input("Choose Mario's action (left, right, or jump): ").lower()  # User input
        
        if action == "jump":
            mario = jump_and_collect_coins(mario)
        else:
            enemy, enemy_damage = encounter_enemy(action)
            if enemy:
                print(f"Oh no! Mario encountered a {enemy} and took {enemy_damage} damage.")
                mario = calculate_damage(mario, enemy_damage)
            else:
                print("Mario avoided all enemies!")
        
        # Display Mario's stats
        print(f"Mario's health: {mario['health']}, Coins: {mario['coins']}")
        
        # Check if Mario's health reaches 0, end the game
        if mario["health"] <= 0:
            print("Game Over! Mario has been defeated.")
            break

# Ensure main function runs
if __name__ == "__main__":
    main()
