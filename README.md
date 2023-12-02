# Dungeons-and-Dragons-Simulator

This Python application serves as a Dungeon and Dragons (D&D) Query Generator, integrating OpenAI's ChatGPT model to generate responses to user queries related to the D&D universe. The application includes a graphical user interface (GUI) developed using Tkinter.

## Features

- **OpenAI's ChatGPT Integration:** The application leverages OpenAI's ChatGPT engine to provide responses to user queries related to D&D. The `AutoGenFramework` class facilitates communication with the OpenAI API.

- **SQLite Database Connectivity:** The application is connected to an SQLite database (`new_DD_database.db`) to store and retrieve information about various entities in the D&D world, such as persons, enemies, species, etc.

- **Sound Functionality:** The application incorporates sound functions using the Pygame library. It can play background music (`DDMUSIC.mp3`) and various sounds using the `play_sound` and `play_background_music` functions.

- **Dice Rolling Animation:** Users can roll virtual dice by clicking on buttons corresponding to different dice types (`d4`, `d6`, `d8`, `d10`, `d12`, `d20`, `d100`). The application simulates dice rolling and displays the result.

- **Story Generation:** The application can generate D&D-themed stories using the `generate_dnd_story` function. Users input the game state and player action to receive a generated story prompt.

## Database Schema

The SQLite database (`new_DD_database.db`) contains tables for various entities in the D&D world, such as `Person`, `Enemy`, `Species`, and more. The schema is designed to accommodate information about different aspects of the game, such as status, affiliation, attributes, and species.

## How to Use

1. **User Input:** Enter a question related to D&D in the input field provided.

2. **Generate Response:** Click the "Generate" button to get a response. The application first checks if the query is related to the database (e.g., querying persons or enemies). If not, it uses the OpenAI API to generate a response.

3. **Sound Effects:** Enjoy background music and sound effects integrated into the application.

4. **Dice Rolling:** Click on the dice buttons to simulate rolling different types of dice.

5. **Story Generation:** Explore D&D-themed stories by inputting the game state and player action.

6. **Add Person to Database:** Click the "Add Person" button to add a new person to the database. Follow the prompts to input status, affiliation, stats, species, level, and experience.

## Additional Information

- The application allows users to interact with the D&D universe dynamically, combining database information with OpenAI's language model.

- For developers, the code includes comments and clear function names for better understanding and maintenance.

- Make sure to have the necessary dependencies installed before running the application. The code uses OpenAI's GPT API, Tkinter for GUI, Pygame for sound, and PIL for image handling.

Feel free to explore and enhance the application to suit your D&D gaming needs!
