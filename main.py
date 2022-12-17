from player import Player
from story import Story
import os

# we can use term colors
if __name__ == "__main__":
    os.system("color")

player = Player()
story = Story(player)
