# Omega: Escape the Lasers!

Omega is a thrilling 2D platformer game where you, the player, must navigate a series of levels while evading deadly lasers.  Sharpen your reflexes and test your timing as you maneuver through challenging obstacles to reach the exit.

## Installation

### System Requirements

To play Omega, you'll need the following installed on your system:

- Python: Omega is developed using Python. Download and install the latest version of Python from https://www.python.org/downloads/.
- pip: pip is Python's package installer. It's usually included with Python installation. Verify its presence by opening a terminal and typing pip ```--version```. If not installed, refer to Python's documentation for installation instructions.

### Getting Started

**1. Clone the Repository:**

Open a terminal or command prompt and navigate to your desired directory. Use the following command to clone the Omega game repository from GitHub:

```sh
git clone https://github.com/ulysses-o/omega
```

This will download the game's source code to a folder named "omega" in your current directory.

**2. Install Dependencies:**

Navigate to the downloaded Omega directory using the ```cd``` command:

```sh
cd omega
```

Within the Omega directory, install the required Python library using pip:

```sh
pip install pygame
```

Pygame is a popular library for creating games in Python.

**3. Run the Game:**

Once the dependencies are installed, you're ready to play! Execute the main Python script using the following command:

```sh
python main.py
```

The game should launch in a new window.

### Gameplay

Omega is a classic 2D platformer where you control the player character. Use the arrow keys on your keyboard to move and jump. Your objective in each level is to reach the exit point while avoiding the red lasers that constantly scan the environment. Touching a laser will result in a game over.

**Level Creation (Optional)**

The provided settings.py file allows you to create your own custom levels for the game.  This is an optional feature for those interested in level design.

**Important Notes:**

- Ensure the map size of your custom level is 22 tiles wide by 14 tiles high.
- Modify the level_dic dictionary within settings.py to represent your level layout.
- Each key in the dictionary corresponds to a level number, and the value is a list representing the tile map.

For detailed instructions on creating custom levels, refer to the comments and documentation within the settings.py file.

**Embrace the Challenge!**

Omega offers a fun and engaging experience for players of all skill levels. Can you navigate the treacherous corridors and escape the relentless lasers? Download Omega today and put your skills to the test!

**Screenshot of Omega game:**

![Ekran Alıntısı](https://user-images.githubusercontent.com/65045005/210205397-415f8388-4685-4f3e-b778-18d7843d0f6e.PNG)
