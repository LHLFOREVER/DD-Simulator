# Data Dictionary File

import random

# Playable Characters and Friendly NPCs
Person = {
    "Status":["Nobility", "Knight", "Civilian", "Criminal"],
    "Affiliation":["Group"],
    "Attributes":["HP","STR","DEX","VIT","INT","SPD"],
    "Species":["Race"],
    "Level":1
    
}

Affiliation = {
    "Group":["Farmer's Guild", "Merchant's Guild", "Labor Union", "Government", "Black Market", "Adventurer's Guild", "Culinary Union","Entertainment Union", "Smithy Guild", "Spiritual Union", "Treasury", "Medical Guild", "Researchers Union", "Teacher's Union", "Education Association", "Military", "Service Union"],   
}

Species = {
    "Race":["Elf","Half-Elf", "Dwarf", "Fairy", "Human", "Draconian", "Beastkind","Demon", "Hybrid", "Angel", "Undead", "Vampire", "Werewolf"]
}
Attributes = {
    "HP": 1,
    "STR":1,
    "DEX":1,
    "VIT":1,
    "INT":1,
    "SPD":1
}

Status = {
    "Nobility":["Rank","Nobility Status"],
    "Knight": ["False", "True", "Rank"],
    "Civilian":["Civilian Status"],
    "Criminal": ["False", "True"],
    "Adventurer": ["Adventurer Status", "Rank", "Role"]
}

Civilian  = {
    "Civilian Status": ["False", "True"]
}

Adventurer = {
    "Adventurer Status": ["False", "True"],
    "Rank": ["Copper", "Iron","Bronze", "Silver", "Amethyst", "Gold", "Emerald", "Corundum", "Diamond", "Platinum"],
    "Role": ["Mage", "Rogue", "Brawler", "Archer", "Sniper"]
}

Knight = {
    "Weapon":["Sword","Greatsword"],
    "Rank":["Royal Guard", "General", "Captain","Commander","Team Leader","Infantry","None"]
}

Nobility = {
    "Rank": ["Royal Family", "Duke", "Duchess", "Marquess", "Marchioness", "Count", "Countess", "Viscount", "Viscountess", "Baron", "Baroness"],
    "Nobility Status":["False", "True", "Fallen"],
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


for loc in Environment.get("location"):
    if Environment.get("Location") == "Villian's Castle" or "Temple" or "Adventurer's Guild":
        LocSize["size"] = "Medium"
    elif Environment.get("Location") == "Dark Cave" or "Dungeon":
        LocSize["size"] = "Large"
    else:
        LocSize["size"] = "Small"

# Determining Building Size
if LocSize.get("size") == "Large":
    Floors = random.randint(11,100)
    Rooms = random.randint(11,100)
elif LocSize.get("size") == "Medium":
    Floors = random.randint(4,10)
    Rooms = random.randint(4,10)
else:
    Floors = random.randint(1,3)
    Rooms = random.randint(1,3)



# Enemies

Wild_Mobs = {
    "wild":["slime","goblin", "zombie", "orc", "constructs"]
}

Thinker_Mobs = {
    "thinker":["bandit", "robot", "robber", "villian's servant"]
}
