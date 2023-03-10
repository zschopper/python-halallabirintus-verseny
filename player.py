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
        self.printout_charsheet()

    def luck_test(self):
        if not self.luck:
            print("Elfogyott a szerencséd!")
            return False
        else:
            success = roll(2) < self.luck
            self.luck -= 1
            if success:
                printc(f"Szerencséd volt! %HEADER%{self.luck}%ENDC% SZERENCSÉD maradt!")
            else:
                printc(f"Nem volt szerencséd! %HEADER%{self.luck}%ENDC% SZERENCSÉD maradt!")
            return success

    def damage(self, amount):
        self.hp -= amount
        printc(f"%RED%{amount}%ENDC% ÉLETERŐ pontot sebződtél, %ORANGE%{self.hp}%ENDC% ÉLETERŐ pontod maradt.")
        return self.hp > 0

    def loot(self, item, amount):
        if item in self.inventory:
            self.inventory[item] += amount
        else:
            self.inventory[item] = amount
        printc(f"%GREEN%{amount} {item}%ENDC% bekerült a leltáradba, most már %WHITE%{self.inventory[item]}%ENDC% {item} van nálad.")

    def printout_charsheet(self):
        printc("\n~~~ %ORANGE%Karakterlap:%ENDC% ~~~")
        printc(f"Ügyesség:  %WHITE%{self.dex:>2}%ENDC%")
        printc(f"Életerő:   %WHITE%{self.hp:>2}%ENDC%")
        printc(f"Szerencse: %WHITE%{self.luck:>2}%ENDC%")
        print("\nTárgyak:")

        if len(self.inventory):
            for key, item in self.inventory.items():
                printc(f"%YELLOW%{item}%ENDC% db %YELLOW%{key}%ENDC%")
        else:
            print("Nincs nálad semmi.")
        print("~~~~~~~~~~~~~~~~~~~~\n")
