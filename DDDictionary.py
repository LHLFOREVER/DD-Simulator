# Data Dictionary File

import random

# Playable Characters and Friendly NPCs
Person = {
    "Status":["Nobility", "Knight", "Civilian", "Criminal"],
    "Affiliation":["Group"],
    "Attributes":["HP","STR","DEX","VIT","INT","SPD"],
    "Species":["Race"],
    "Level":1,
    "Experience":0
    
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


Enemy = {
    "Status":["Nobility", "Knight", "Civilian", "Criminal"],
    "Affiliation":"Chaos",
    "Attributes":["HP","STR","DEX","VIT","INT","SPD"],
    "Species":["Wild_Mobs, Thinker_Mobs"],
    "Level":1,
    "Experience":0
    
}

#Mobs 
Wild_Mobs = {
    "wild":["slime","goblin", "zombie", "orc", "construct", "skeleton"]
}

Thinker_Mobs = {
    "thinker":["bandit", "robot", "robber", "villian's servant", "dragon", "vampire"]
}


#Weapons:

Weapon = {
    "sword":["shortsword", "longsword", "katana","broadsword", "rapier"],
    "bow":["crossbow", "recurve bow", "long bow", "shortbow"],
    "knife":["dagger", "knife"],
    "heavy":["hammer", "club", "mace"],
    "spear":["spear", "polearm"],
    "wand":["wand", "staff"],
    "gun":["pistol", "hunter rifle", "magic rifle"]
}


Environment = {
    "Region": ["Human Kingdom", "The Wilds", "Small Village", "Elven Forest", "Elven Kingdom", "Dwarven Kingdom", "Religious Grounds", "Dragon's Lair", "Demon Realm"],
    "Location":["Adventurer's Guild", "Restaurant", "Inn","Townperson's Home", "Hut", "Villian's Castle", "Dark Cave", "Dungeon", "Temple", "Garden", "Dark Alley", "Flower Shop", "Cafe" ],
}

LocSize = {
    "size":["Small", "Medium", "Large"],
}

#DOT is Damage Over Time
BuffsnDebuffs = {
    "speed": {"extra action", "extra movement", "warp", "acceleration"},
    "slow": {"sluggish", "exhausted", "stun", "chained", "panic"}, 
    "DOT": {"poison","frostbite","shock"},
    "redirect":{"charm", "blind", "haze"},
    "ally_debuff":{"betray","corpse explosion"},
    "self_debuff": {"dull", "fragile", "vulnerable", "weak"},
    "self_buff":{"absorption", "armor", "berserk", "bloodlust", "defense", "dodge", "elasiticity", "focus", "fury", "hatred", "immortality",
                "immunity", "merciless", "mirror", "regen", "shell", "shield", "taunt", "thorn", "vampire"}
}

Multiplier = {
    "buff":{"1.0x", "1.2x", "1.5x"},
    "debuff":{"0.75x", "0.5x", "0.25x"} 
}








