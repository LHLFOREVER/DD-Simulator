# Data Dictionary File

import random

# Playable Characters and Friendly NPCs
Person = {
    "Status":["Nobility", "Knight", "Civilian", "Criminal"],
    "Affiliation":["Group"],
    "Attributes":["HP","STR","DEX","STA","INT","SPD"],
    "Species":["Race"],
    "Level":1,
    "Experience":0
    
}

Affiliation = {
    "Group":["Farmer's Guild", "Merchant's Guild", "Labor Union", "Government", "Black Market", "Adventurer's Guild", "Culinary Union","Entertainment Union", "Smithy Guild", "Spiritual Union", "Treasury", "Medical Guild", "Researchers Union", "Teacher's Union", "Education Association", "Military", "Service Union"],   
}

Species = {
    "Race":["Elf","Half-Elf", "Dwarf", "Fairy", "Human", "Draconian", "Beastkind","Demon", "Hybrid", "Angel", "Undead", "Vampire", "Werewolf", "Goblin", "Slime", "Orc", "Zombie",]
}
Attributes = {
    "HP": 1,
    "STR": 1,
    "DEX": 1,
    "STA": 1,
    "INT": 1,
    "SPD": 1
}

Status = {
    "Nobility": ["Rank","Nobility Status"],
    "Knight": [False, True],
    "Civilian": ["Civilian Status"],
    "Criminal": [False, True],
    "Adventurer": ["Adventurer Status", "Rank", "Role"]
}

Civilian  = {
    "Civilian Status": [False, True]
}

Adventurer = {
    "Adventurer Status": [False, True],
    "Rank": ["Copper", "Iron","Bronze", "Silver", "Amethyst", "Gold", "Emerald", "Corundum", "Diamond", "Platinum"],
    "Role": ["Mage", "Rogue", "Brawler", "Archer", "Sniper"]
}

Knight = {
    "Rank":["Royal Guard", "General", "Captain","Commander","Team Leader","Infantry","None"]
}

Nobility = {
    "Rank": ["Royal Family", "Duke", "Duchess", "Marquess", "Marchioness", "Count", "Countess", "Viscount", "Viscountess", "Baron", "Baroness", "Fallen"],
    "Nobility Status":[False, True]
}




# Environment
Environment = {
    "Region": ["Human Kingdom", "The Wilds", "Small Village", "Elven Forest", "Elven Kingdom", "Dwarven Kingdom", "Religious Grounds", "Dragon's Lair", "Demon Realm"],
    "Location":["Adventurer's Guild", "Restaurant", "Inn","Townperson's Home", "Hut", "Villian's Castle", "Dark Cave", "Dungeon", "Temple", "Garden", "Dark Alley", "Flower Shop", "Cafe" ],
}

LocSize = {
    "size":["Small", "Medium", "Large"],
}
Floors = 0
Rooms = 0
def location_build(place):
    for place in Environment["Location"]:
        if Environment["Location"] == ("Villian's Castle" or "Temple" or "Adventurer's Guild"):
            LocSize["size"] = "Medium"
        elif Environment["Location"] == ("Dark Cave" or "Dungeon"):
            LocSize["size"] = "Large"
        elif Environment["Location"] != ("Dark Cave" or "Dungeon" or "Villian's Castle" or "Temple" or "Adventurer's Guild"):
            LocSize["size"] = "Small"
        else:
            return("Please enter a valid location.")

# Determining Building Size
    if LocSize["size"] == "Large":
        Floors = random.randint(11,100)
        Rooms = random.randint(11,100)
    elif LocSize["size"] == "Medium":
        Floors = random.randint(4,10)
        Rooms = random.randint(4,10)
    else:
        Floors = random.randint(1,3)
        Rooms = random.randint(1,3)
    return Floors, Rooms

location_build("Temple")



#Weapons:

Weapon = {
    "sword":[False, True],
    "greatsword":[False, True],
    "staff":[False, True],
    "wand":[False, True],
    "katana":[False, True],
    "scythe":[False, True],
    "rifle":[False, True],
    "handgun":[False, True],
    "bow":[False, True],
    "crossbow":[False, True],
    "melee":[False, True],
    "magi-gun":[False, True]       
}



#Actions

Action = {
    "Movement": ["teleport", "walk", "run", "sprint", "return"],
    "Attack":[False, True],
    "Defend":["block"],
    "Counter":["parry", "cancel"],
    "Dodge":["dodge"]
}
def attack_action(weapon):
    move = ''
    if weapon["sword"] == True:
        move =  "swing"
    elif weapon["staff","wand", "magi-gun"] == True:
        move = "cast"
    elif weapon["bow","crossbow","handgun","rifle"] == True:
        move = "shoot"
    elif weapon["melee"] == True:
        move = "brawl" 
    else:
        return "Please choose a valid weapon or make a new one!"
    return move

assert attack_action("sword") == "swing", "attack_action() is not functioning as intended"








