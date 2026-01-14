import random

# Player Stats

player_name = ""
health = 100
strength = 4
awareness = 7
inventory = []

# story flags (simple True/False)
helped_hart = False
rowan_with_you = False

# Helper Functions

def pause():
    """Just wait for user to continue."""
    input("\nPress Enter to continue...\n")



def show(text):
    """Simple function to print story text."""
    print("\n" + text + "\n")

def choose(options):
    """Shows a list of choices and returns the number they pick."""
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    choice = input("Choice: ")
    while not choice.isdigit() or int(choice) < 1 or int(choice) > len(options):
        choice = input("Enter a valid choice number: ")
    return int(choice)

def add_item(item):
    inventory.append(item)
    print(f"> You got: {item}")


def fight(enemy, enemy_hp):
    """Simple combat based on random damage and strength."""
    global health

    show(f"A {enemy} appears!")

    while enemy_hp > 0 and health > 0:
        print(f"Your health: {health} | {enemy} health: {enemy_hp}")
        action = choose(["Attack", "Use Med Injector", "Try to Run"])

        if action == 1:
            dmg = random.randint(3, 3 + strength)
            enemy_hp -= dmg
            print(f"You hit the {enemy} for {dmg} damage.")
        elif action == 2:
            if "Med Injector" in inventory:
                inventory.remove("Med Injector")
                health += 20
                if health > 100:
                    health = 100
                print("You used a Med Injector.")
            else:
                print("You don't have one.")
        else:
            if random.random() < 0.4:
                print("You escaped!")
                return True
            else:
                print("You couldn't escape!")

        if enemy_hp > 0:
            enemy_dmg = random.randint(4, 9)
            health -= enemy_dmg
            print(f"The {enemy} hits you for {enemy_dmg} damage.")

        print()

    if health <= 0:
        show("You fall to the ground and everything goes dark...")
        return False
    else:
        show(f"You defeated the {enemy}!")
        return True


# Story Scenes

def intro_scene():
    global player_name, health, strength

    show("You wake up strapped to a cold metal table. Red lights flash around you.")
    show("A robotic voice says: 'DOE Facility 12B – Subject #727 unstable.'")

    player_name = input("You try to remember your name. What is it? ")
    if player_name.strip() == "":
        player_name = "Subject 727"

    show(f"You are {player_name}. Your head hurts and you don't remember much.")

    choice = choose(["Try to slip out of the straps quietly.",
                     "Rip the straps off with force."])

    if choice == 1:
        show("You slowly pull free without making noise.")
    else:
        show("You pull hard and break the straps, hurting yourself a bit.")
        health -= 5
        strength += 1
        add_item("Metal Strap")
        print(f"Your health is now {health}.")

    pause()

def surveillance_atrium():
    global health

    show("You enter a huge room full of screens showing random people in the city.")
    show("A tall security drone (Aegis-4) stands in the middle of the room.")

    action = choose(["Try to hack Aegis-4 from a console.",
                     "Sneak around it.",
                     "Attack it first."])

    hostile = False
    if action == 1:
        chance = 0.4 + (awareness / 20)
        if random.random() < chance:
            show("You hack Aegis-4. Its lights turn blue. It will not attack you.")
        else:
            show("The hack fails. Aegis-4 turns hostile!")
            hostile = True
    elif action == 3:
        hostile = True
    else:
        show("You sneak along the side of the room.")

    if hostile:
        alive = fight("Aegis-4", 30)
        if not alive:
            return False

    # Puzzle 1 (simple)
    show("A locked door blocks your path. Three lights blink: top, bottom, middle.")
    code = input("Enter the 3-digit code (1=top, 2=middle, 3=bottom): ")

    if code.strip() == "313":
        show("The door unlocks quietly.")
    else:
        show("Alarm goes off! Guards run in!!!")
        alive = fight("Security Guard", 25)
        if not alive:
            return False

    add_item("Level-2 Keycard")
    add_item("Med Injector")
    pause()
    return True


def energetics_lab():
    global helped_hart, awareness
    show("You enter a lab full of cables and weird headgear.")
    show("A scientist looks up. 'I'm Dr. Hart,' she says nervously.")

    action = choose(["Ask what is happening.",
                     "Ignore her and search the room.",
                     "Tell her to help you."])

    if action == 1:
        show("'You were part of a test,' she says. 'They changed your awareness level.'")
    elif action == 2:
        show("You search the room for supplies.")
    else:
        show("'Okay! I'll help,' she says.")

    # Do you help her?
    action2 = choose(["Help Dr. Hart.", "Leave her behind."])
    if action2 == 1:
        helped_hart = True
        show("She nods. 'Meet me near the reactor later.'")
    else:
        helped_hart = False
        show("You walk away. She mumbles something you can't hear.")


    # Puzzle 2 (simple)
    show("You find 3 log files labeled Day 1, Day 90, Day 30 but in wrong order.")
    order = input("Type the correct order (like: 1,30,90): ")

    if order.replace(" ", "") == "1,30,90":
        show("You organize the logs. Your awareness increases a bit.")
        awareness += 1
    else:
        show("You skim the files but don't understand everything.")

    add_item("Override Chip")
    pause()
    return True


def meet_rowan():
    global rowan_with_you

    show("A young guy crawls out of a vent. 'I'm Rowan,' he says.")
    show("He says he came to expose the lab and can help you escape.")

    choice = choose(["Let Rowan join you.",
                     "Tell him to go his own way.",
                     "Don't trust him."])

    if choice == 1:
        rowan_with_you = True
        show("'Alright,' Rowan says. 'Stick with me.'")
    else:
        rowan_with_you = False
        show("Rowan shrugs and disappears into another duct.")

    pause()


def server_spine():
    show("You reach the Server Spine. It's freezing and full of cables.")
    show("This place controls everything in the facility.")

    options = ["Help Rowan hack the servers.",
               "Help Dr. Hart overload the reactor.",
               "Listen to Director Kael.",
               "Use Override Chip to talk to the Overseer AI."]

    choice = choose(options)

    if choice == 1 and rowan_with_you:
        ending_a()
    elif choice == 2 and helped_hart:
        ending_b()
    elif choice == 3:
        ending_c()
    else:
        ending_d()

# Endings


def ending_a():
    show("You and Rowan run to the Transit Dock and upload the files.")
    show("People in the city see the experiments on every screen.")
    show("ENDING A: You started a rebellion.")
    pause()

def ending_b():
    show("You and Dr. Hart overload the reactors. The whole lab shakes.")
    show("You escape in a small escape pod before it explodes.")
    show("ENDING B: The facility is destroyed.")
    pause()

def ending_c():
    show("Director Kael says you were designed to serve the government.")
    show("You decide to join him and become an Authority agent.")
    show("ENDING C: You enforce the system.")
    pause()


def ending_d():
    show("You connect to the Overseer. Your mind begins to merge with the AI.")
    show("You spread across every camera and sensor in the city.")
    show("ENDING D: You become the Overseer.")
    pause()



# MAIN GAME

def main():
    intro_scene()

    alive = surveillance_atrium()
    if not alive or health <= 0:
        return

    alive = energetics_lab()
    if not alive or health <= 0:
        return

    meet_rowan()
    server_spine()

main()
