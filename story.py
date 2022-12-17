import json
from dice import roll
from printc import printc

class Story:

    def __init__(self, player):
        self.room = "1"
        self.finished = False

        self.player = player
        with open("story.json", "r", encoding="utf-8") as fh:
            self.storyline = json.load(fh)
        self.start()

    def start(self):
        self.loop(1)  # start
        # self.loop(387)  # combat
        # self.loop(270)  # loot
        # self.loop(215) # loc. damage

    def loop(self, room=None):
        if room is not None:
            self.room = str(room)
        while not self.finished:
            self.location = self.storyline[self.room]
            self.output_location()
            self.handle_damage()
            self.handle_loot()
            self.handle_combat()
            if not self.finished:
                self.handle_actions()

    def output_location(self):
        if 'title' in self.location:
            printc(self.location['title'])
        else:
            printc(f"~~~ %WHITE%{self.room}%ENDC%. oldal ~~~")
        printc(self.location['description'])

    def handle_damage(self):
        if 'damage' in self.location:
            self.player.damage(self.location['damage'])

    def handle_loot(self):
        if 'loots' in self.location:
            loots = self.location['loots']
            for loot in loots:
                self.player.loot(loot['name'], int(loot['amount']))

    def handle_combat(self):
        if 'encounter' in self.location:
            mons = self.location['encounter']
            mons_name = mons['name']
            mons_hp = mons['stats']['hp']
            mons_dex = mons['stats']['dex']
            combat_ended = False
            while not combat_ended:
                player_strike = roll(2, self.player.dex)
                mons_strike = roll(2, mons_dex)
                printc(f"A te dobásod %WHITE%{player_strike}%ENDC% volt!")
                printc(f"A {mons_name} dobása %WHITE%{mons_strike}%ENDC% volt!")

                if player_strike > mons_strike:  # PLAYER DEALS DAMAGE
                    printc(f"%GREEN%Eltaláltad%ENDC% a(z) {mons['name']}-t!")
                    use_luck = input("Szeretnl szerencsét felhasználni a sebzés duplázásához? ").upper() == 'I'
                    if use_luck:
                        if self.player.luck_test():
                            mons_hp -= 4  # luck damage
                        else:
                            mons_hp -= 1  # no luck damage
                    else:
                        mons_hp -= 2  # normal damage
                elif player_strike < mons_strike:  # MONSTER DEALS DAMAGE
                    printc(f"A(z) {mons['name']} %RED%eltalált%ENDC% téged!")
                    use_luck = input("Szeretnél szerencsét felhasználni a sebződés csökkentéséhez? ").upper() == ['I']
                    if use_luck:
                        if self.player.luck_test():
                            self.player.damage(1)  # luck damage
                        else:
                            self.player.damage(3)  # no luck damage
                    else:
                        self.player.damage(2)  # normal damage
                else:  # NO DAMAGE
                    print("Kivédtétek egymás támadását!")
                if self.player.hp <= 0:
                    printc("%RED%Meghaltál.%ENC%")
                    self.finish()
                if mons_hp <= 0:
                    printc(f"%CYAN%Megölted%ENDC% a(z) {mons_name}-t.")
                printc(f"Életerőd: %RED%{self.player.hp}%ENDC% Ügyességed: %YELLOW%{self.player.dex}%ENDC% Szerencséd: %GREEN%{self.player.luck}%ENDC%")

                combat_ended = self.player.hp <= 0 or mons_hp <= 0

    def handle_actions(self):
        if 'exits' not in self.location:  # if there is no exit, the game has finished
            self.finish()
        else:
            exits = self.location['exits']

            moved = False
            while not moved:
                print("Mit szeretnél csinálni?\n")
                print("k - A karakter lap megtekintése")
                i = 0
                while i < len(exits):
                    printc(f"{i+1} - lapozás a %YELLOW%{exits[i]}%ENDC%. oldalra")
                    i += 1
                else:
                    moved = True

                action = input("Mi a választásod? ").lower()
                if action.isnumeric():
                    if int(action) <= len(exits):
                        moved = True
                        self.room = str(exits[int(action) - 1])
                else:
                    if action == "k":
                        self.player.printout_charsheet()

    def finish(self):
        self.finished = True
        print("~~~ vége ~~~~")
