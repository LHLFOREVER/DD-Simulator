import sqlite3

def create_new_database():
    # Connect to the database (this will create the database file if it doesn't exist)
    conn = sqlite3.connect('new_DD_database.db')
    cursor = conn.cursor()

    # Create the Person table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Person (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Status TEXT,
        Affiliation TEXT,
        HP INTEGER,
        STR INTEGER,
        DEX INTEGER,
        VIT INTEGER,
        INT INTEGER,
        SPD INTEGER,
        Species TEXT,
        Level INTEGER,
        Experience INTEGER
    );
    ''')

    # Create other tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Affiliation (
        ID INTEGER PRIMARY KEY,
        GroupName TEXT
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Species (
        ID INTEGER PRIMARY KEY,
        Race TEXT
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Status (
        ID INTEGER PRIMARY KEY,
        StatusType TEXT,
        Attribute1 TEXT,
        Attribute2 TEXT,
        Attribute3 TEXT
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Civilian (
        ID INTEGER PRIMARY KEY,
        CivilianStatus TEXT
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Adventurer (
        ID INTEGER PRIMARY KEY,
        AdventurerStatus TEXT,
        Rank TEXT,
        Role TEXT
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Knight (
        ID INTEGER PRIMARY KEY,
        Weapon TEXT,
        Rank TEXT
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Nobility (
        ID INTEGER PRIMARY KEY,
        Rank TEXT,
        NobilityStatus TEXT
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Enemy (
        ID INTEGER PRIMARY KEY,
        Status TEXT,
        Affiliation TEXT,
        HP INTEGER,
        STR INTEGER,
        DEX INTEGER,
        VIT INTEGER,
        INT INTEGER,
        SPD INTEGER,
        Species TEXT,
        Level INTEGER,
        Experience INTEGER
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Wild_Mobs (
        ID INTEGER PRIMARY KEY,
        MobType TEXT
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Thinker_Mobs (
        ID INTEGER PRIMARY KEY,
        MobType TEXT
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Weapon (
        ID INTEGER PRIMARY KEY,
        WeaponType TEXT,
        SubType TEXT
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Environment (
        ID INTEGER PRIMARY KEY,
        Region TEXT,
        Location TEXT
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS LocSize (
        ID INTEGER PRIMARY KEY,
        Size TEXT
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS BuffsnDebuffs (
        ID INTEGER PRIMARY KEY,
        BuffType TEXT,
        BuffName TEXT
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Multiplier (
        ID INTEGER PRIMARY KEY,
        MultiplierType TEXT,
        Value TEXT
    );
    ''')

    # Save (commit) the changes
    conn.commit()

    # Close the connection
    conn.close()

    print("Database and tables created successfully.")

# Run the function to create the database and tables
create_new_database()
