# Data Dictionary File

Person = {
    "Status":["Nobility", "Knight", "Civilian", "Criminal"],
    "Affiliation":["Group", "Job"],
    "Job":["Group", "Salary","Years Experience"]
}

Affiliation = {
    "Group":["Farmer's Guild", "Merchant's Guild", "Labor Union", "Government", "Black Market", "Adventurer's Guild", "Culinary Union","Entertainment Union", "Smithy Guild", "Spiritual Union", "Treasury", "Medical Guild", "Researchers Union", "Teacher's Union", "Education Association", "Military", "Service Union"],
    
}

Group = {
    "Farmer's Guild":[],
    "Merchant's Guild":[],
    "Labor Union":[],
    "Government":[],
    "Black Market":[],
    "Adventurer's Guild":[],
    "Culinary Union":[],
    "Entertainment Union":[],
    "Smithy Guild":[],
    "Spiritual Union":[],
    "Treasury":[],
    "Medical Guild":[],
    "Researchers Union":[],
    "Teacher's Union":[],
    "Education Association":[],
    "Military":[],
    "Service Union":[]



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