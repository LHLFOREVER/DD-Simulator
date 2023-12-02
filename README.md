# Dungeons-and-Dragons-Simulator

This Python application serves as a Dungeon and Dragons (D&D) Query Generator, integrating OpenAI's ChatGPT model to generate responses to user queries related to the D&D universe. The application includes a graphical user interface (GUI) developed using Tkinter.

## Prerequisites

Before running the application, ensure you have the following:

- **OpenAI API Key:** Obtain your API key from [OpenAI](https://beta.openai.com/signup/) and replace the placeholder in the code with your key.

- **Dependencies:** Install the necessary dependencies using the following:
  ```bash
  pip install openai pygame pillow
  ```

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

6. **Add Person to Database:** Click the "Add Person" button to add a new person to the database. Follow the prompts to input status, affiliation, species, level, and experience.

## Imports

This section provides an overview of each import statement in the project, outlining the purpose and functionality of the imported modules.

```python
import openai
import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
import time
import random
import DDDictionary
from DDDictionary import *
import sqlite3
import pygame
  ```

##### 1. `import openai`

- **Purpose:** This import brings in the `openai` library, allowing interaction with OpenAI's GPT-3 API. The library is used to generate responses to user queries related to the D&D universe.

##### 2. `import tkinter as tk`

- **Purpose:** This import brings in the `tkinter` library, which is the standard GUI (Graphical User Interface) toolkit for Python. It provides the foundation for creating the application's user interface.

##### 3. `from tkinter import simpledialog, messagebox`

- **Purpose:** This import includes specific modules (`simpledialog` and `messagebox`) from the `tkinter` library. These modules are used for creating dialog boxes that prompt users for input and display messages, respectively.

##### 4. `from PIL import Image, ImageTk`

- **Purpose:** This import includes the `Image` and `ImageTk` modules from the Python Imaging Library (PIL). These modules are utilized for working with images, particularly for displaying background images in the Tkinter GUI.

##### 5. `import time`

- **Purpose:** The `time` module is a standard Python library for working with time-related functions. In this project, it is used to introduce delays during the simulated dice rolling animation.

##### 6. `import random`

- **Purpose:** The `random` module is a standard Python library for generating pseudo-random numbers. In this project, it is used to simulate dice rolling and provide random outcomes.

##### 7. `import DDDictionary`

- **Purpose:** This import brings in the `DDDictionary` module, which presumably contains dictionaries or data structures defining aspects of the D&D universe. 

##### 8. `from DDDictionary import *`

- **Purpose:** This import includes all objects (functions, variables, classes) defined in the `DDDictionary` module into the current namespace. It is a convenient way to make the content of `DDDictionary` accessible without specifying each item explicitly.

##### 9. `import sqlite3`

- **Purpose:** The `sqlite3` module is a Python library for interacting with SQLite databases. In this project, it is used to connect to and query a database (`new_DD_database.db`) containing information about entities in the D&D world.

##### 10. `import pygame`

- **Purpose:** The `pygame` library is used for adding sound functionality to the application. It provides tools for working with multimedia elements, such as playing background music and sound effects.

These imports collectively contribute to the functionality of the D&D Query Generator, providing tools for GUI development, image handling, database connectivity, random number generation, and multimedia integration.

## Additional Information

- The application allows users to interact with the D&D universe dynamically, combining database information with OpenAI's language model.

- For developers, the code includes comments and clear function names for better understanding and maintenance.

- Make sure to replace the placeholder API key with your own before running the application.

Feel free to explore and enhance the application to suit your D&D gaming needs!
