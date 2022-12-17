import json
from dice import roll
from printc import printc

class Story:

    def __init__(self, player):
        self.room = 0
        self.finished = False

        self.player = player
        with open("story.json", "r", encoding="utf-8") as fh:
            self.storyline = json.load(fh)
        self.start()

    def start(self):
        self.move(1)  # start
        # self.move(387)  # combat
        # self.move(270)  # loot
        # self.move(215)

    def move(self, room):
        if str(room) not in self.storyline:
            print("Érvénytelen választás!")
            result = False
        else:
            self.room = str(room)

            self.location = self.storyline[self.room]

            self.output_location()
            self.handle_damage()
            self.handle_loot()
            self.handle_combat()
            if not self.finished:
                self.handle_actions()
            result = True
        return result

    def output_location(self):
        if 'title' in self.location:
            print(self.location['title'])
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
                    print(f"Eltaláltad a(z) {mons['name']}-t!")
                    use_luck = input("Szeretnél szerencsét felhasználni a sebzés duplázásához? ").upper() == 'I'
                    if use_luck:
                        if self.player.luck_test():
                            mons_hp -= 4  # luck damage
                        else:
                            mons_hp -= 1  # no luck damage
                    else:
                        mons_hp -= 2  # normal damage
                elif player_strike > mons_strike:  # MONSTER DEALS DAMAGE
                    print(f"A(z) {mons['name']} %RED%eltalált téged!")
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
                    printc(f"%CYAN%Megölted a(z) {mons_name}-t.%ENDC%")
                    self.finish()

                combat_ended = self.player.hp <= 0 or mons_hp <= 0

    def handle_actions(self):
        moved = False
        while not moved:
            print("Mit szeretnél csinálni?\n")
            print("k - A karakter lap megtekintése")
            exits = []
            if 'exits' in self.location:
                exits = self.location['exits']
                i = 0
                while i < len(exits):
                    print(f"{i+1} - lapozás a {exits[i]}. oldalra")
                    i += 1
            action = input("Mi a választásod? ").lower()
            if action.isnumeric():
                if int(action) <= len(exits):
                    moved = True
                    self.move(exits[int(action) - 1])
            else:
                if action == "k":
                    self.player.printout_charsheet()

    def finish(self):
        self.finished = True
        print("~~~ vége ~~~~")
