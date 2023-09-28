# Data Dictionary File

import random


Person = {
    "Status":["Nobility", "Knight", "Civilian", "Criminal"],
    "Affiliation":["Group"],
    "Attributes":["HP","STR","DEX","VIT","INT","SPD"],
    "Species":["Race"]
    
}

Affiliation = {
    "Group":["Farmer's Guild", "Merchant's Guild", "Labor Union", "Government", "Black Market", "Adventurer's Guild", "Culinary Union","Entertainment Union", "Smithy Guild", "Spiritual Union", "Treasury", "Medical Guild", "Researchers Union", "Teacher's Union", "Education Association", "Military", "Service Union"],   
}

Species = {
    "Race":["Elf","Half-Elf", "Dwarf", "Fairy", "Human", "Draconian", "Beastkind","Demon", "Hybrid", "Angel", "Undead", "Vampire", "Werewolf"]
}
Attributes = {
    "HP":[],
    "STR":[],
    "DEX":[],
    "VIT":[],
    "INT":[],
    "SPD":[]
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


Environment = {
    "Region": ["Human Kingdom", "The Wilds", "Small Village", "Elven Forest", "Elven Kingdom", "Dwarven Kingdom", "Religious Grounds", "Dragon's Lair", "Demon Realm"],
    "Location":["Adventurer's Guild", "Restaurant", "Inn","Townperson's Home", "Hut", "Villian's Castle", "Dark Cave", "Dungeon", "Temple", "Garden", "Dark Alley", "Flower Shop", "Cafe" ],
    "Locsize":["Size", "Floors", "Rooms"]
}

LocSize = {
    "size":["Small", "Medium", "Large"],
}
Floors = []
Rooms =[]

if LocSize == "Large":
    Floors = random.randint(11,100)
    Rooms = random.randint(11,100)
elif LocSize == "Medium":
    Floors = random.randint(4,10)
    Rooms = random.randint(4,10)
else:
    Floors = random.randint(1,3)
    Rooms = random.randint(1,3)


