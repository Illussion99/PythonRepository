#!/usr/bin/env python3

class Bottle():

    def __init__(self, name, volume, content_type, manufacturer, proof, price):
        self._name = name
        self._volume = volume 
        self._content_type = content_type
        self._manufacturer = manufacturer
        self._proof = proof 
        self._price = price

    def to_string(self):
        return f"{self._name:^12} | {str(self._volume) + "l":^4} | {self._content_type:^8} | {self._manufacturer:^14} | {str(self._proof) + "%":^5} | {str(self._price) + "€":^5}"

class BottleShelf():

    def __init__(self):
        self._bottles = []

    def add_bottle(self, bottle):
        self._bottles.append(bottle)

    def add_bottles(self, bottles):
        for bottle in bottles:
            self._bottles.append(bottle)

    def remove_bottle(self, bottle):
        self._bottles.remove(bottle)

    def find_by_name(self, bottle_name):
        for bottle in self._bottles:
            if bottle._name.lower() == bottle_name.lower():
                return bottle

        return None

    def to_string(self):
        returned_string = "|‾‾‾‾‾‾‾‾‾‾‾‾|‾‾‾‾|‾‾‾‾‾‾‾‾|‾‾‾‾‾‾‾‾‾‾‾‾‾‾|‾‾‾‾‾|‾‾‾‾‾|\n"
        returned_string += "|    NAME    | l. |  TYPE  | MANUFACTURER | PRF | PRC |\n"

        for bottle in self._bottles:
            returned_string += bottle.to_string()
            returned_string += "\n"

        returned_string += "|____________|____|________|______________|_____|____|\n"

        return returned_string

    def seed(self):
        self.add_bottle(Bottle("Jack Daniels", 0.7, "whiskey", "Brown-Borman", 42, 20))
        self.add_bottle(Bottle("Jaeger", 0.5, "liquor", "Wolfenbuttel", 37, 14))
        self.add_bottle(Bottle("Slivovica", 1, "spirit", "Dedko", 72, 10))

    def welcome():
        print("\nWelcome to Bottle Shelf.\n")
        print("Please make a choice: ")
        print(" 1. List content ")
        print(" 2. Add a bottle ")
        print(" 3. Remove a bottle ")
        print(" 4. Find a bottle ")
        print(" q. Exit ")

    def menu(shelf):
        welcome()
        choice = input("Input: ")

        if choice[0] == "1":
            print(shelf.to_string)

        elif choice[0] == "2":
            name = input("Enter bottle name: ")
            volume = float(input("Enter volume (l): "))
            content_type = input("Enter alc. type: ")
            manufacturer = input("Enter manufacturer: ")
            proof = int(input("Enter proof/alc.&: "))
            price = int(input("Enter price (€): "))

            shelf.add_bottle(Bottle(name, volume, content_type, manufacturer, proof, price))

        elif choice[0] == "3":
                    

        input("Press any key + enter to continue")

if __name__ == "__main__":
    shelf = BottleShelf()
    shelf.seed()

    menu(shelf)