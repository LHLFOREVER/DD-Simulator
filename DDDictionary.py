# Data Dictionary File

Person = {
    "Status":["Nobility", "Knight", "Civilian", "Criminal"]
    "Job":[]
}

Job = {
    
}


Status = {
    "Nobility":["Rank","Nobility Status"],
    "Knight": ["False", "True", "Rank"],
    "Civilian":["Civilian Status"],
    "Criminal": ["False", "True"]
}

Civilian  = {
    "Civilian Status": ["False", "True"],
    "Job" :["Milita", "Farmer","Laborer", "Merchant","Local Official", "Business Owner", "Adventurer"]
}

Adventurer = {
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