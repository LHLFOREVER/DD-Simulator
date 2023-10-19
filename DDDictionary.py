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









