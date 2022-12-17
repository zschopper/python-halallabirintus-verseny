from dice import roll
from printc import printc

class Player:
    def __init__(self):
        self.dex = 0
        self.hp = 0
        self.luck = 0
        self.inventory = {}
        self.gen_stats()

    def gen_stats(self):
        self.dex = roll(1, 6)
        self.hp = roll(2, 12)
        self.luck = roll(1, 6)

    def luck_test(self):
        success = roll(2) < self.luck
        self.luck -= 1
        if success:
            printc(f"Szerencséd volt! %HEADER%{self.luck}%ENDC% SZERENCSÉD maradt!")
        else:
            printc(f"Nem volt szerencséd! %HEADER%{self.luck}%ENDC% SZERENCSÉD maradt!")
        return success

    def damage(self, amount):
        self.hp -= amount
        printc(f"{amount} ÉLETERŐ pontot sebződtél, %ORANGE%{self.hp}%ENDC% ÉLETERŐ pontod maradt.")
        return self.hp > 0

    def loot(self, item, amount):
        if item in self.inventory:
            self.inventory[item] += amount
        else:
            self.inventory[item] = amount
        printc(f"%GREEN%{amount} {item}%ENDC% bekerült a leltáradba, most már %WHITE%{self.inventory[item]}%ENDC% {item} van nálad.")

    def printout_charsheet(self):
        printc("%HEADER%Karakterlap:%ENDC%")
        print(f"Ügyesség: {self.dex}")
        print(f"Életerő: {self.hp}")
        print(f"Szerencse: {self.luck}")
        print("\nTárgyak:")

        if len(self.inventory):
            for key, item in self.inventory.items():
                print(f"{item} db {key}")
        else:
            print("Nincs nálad semmi.")
