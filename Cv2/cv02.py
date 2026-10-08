#!/usr/bin/env python3
import os

class Bottle:

    def __init__(self, name, volume, content_type, manufacturer, proof, price):
        self._name = name
        self._volume = volume
        self._content_type = content_type
        self._manufacturer = manufacturer
        self._proof = proof
        self._price = price

    def to_string(self):
        return (f"|{self._name:^12}|{str(self._volume) + 'l':^4}|"
                f"{self._content_type:^8}|{self._manufacturer:^14}|"
                f"{str(self._proof) + '%':^5}|{str(self._price) + '€':^5}|")


class BottleShelf:

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
            returned_string += bottle.to_string() + "\n"

        returned_string += "|____________|____|________|______________|_____|_____|\n"
        return returned_string

    def seed(self):
        self.add_bottle(Bottle("Jack Daniels", 0.7, "whiskey", "Brown-Borman", 42, 20))
        self.add_bottle(Bottle("Jaeger", 0.5, "liquor", "Wolfenbuttel", 37, 14))
        self.add_bottle(Bottle("Slivovica", 1, "spirit", "Dedko", 72, 10))

    def welcome(self):
        print("\nWelcome to Bottle Shelf.\n")
        print("Please make a choice: ")
        self.command_list()

    def command_list(self):
        print(" 1. List content ")
        print(" 2. Add a bottle ")
        print(" 3. Remove a bottle ")
        print(" 4. Find a bottle ")
        print(" q. Exit ")

    def menu(self):

        self.welcome()

        while True:

            choice = input("Input: ").strip()

            if not choice:
                continue

            c = choice[0].lower()

            if c == "1":
                print(self.to_string())

            elif c == "2":
                name = (input("Enter bottle name: "))[:12]
                volume = str(int(input("Enter volume (l): ")))[:4]
                content_type = (input("Enter alc. type: "))[:8]
                manufacturer = (input("Enter manufacturer: "))[:14]
                proof = str(int(input("Enter proof/alc.%: ")))[:5]
                price = str(float(input("Enter price (€): ")))[:5]

                self.add_bottle(Bottle(name, volume, content_type, manufacturer, proof, price))

            elif c == "3":
                name = input("Enter bottle name: ")
                bottle = self.find_by_name(name)
                if bottle is not None:
                    self.remove_bottle(bottle)
                    print(f"Bottle {name.title()} has been removed")
                else:
                    print(f"No bottle with the name {name.title()} has been found in the shelf")

            elif c == "4":
                name = input("Enter bottle name: ")
                bottle = self.find_by_name(name)
                if bottle is not None:
                    print(bottle.to_string())
                else:
                    print(f"No bottle with the name {name.title()} has been found in the shelf")

            elif c == "q":
                print("Exiting program...")
                exit(0)

            else:
                print("Unknown command! Use one of the following commands: ")
                self.command_list()

            input("\nPress anything + enter to continue!")

            os.system("cls")
            self.command_list()


if __name__ == "__main__":
    shelf = BottleShelf()
    shelf.seed()
    shelf.menu()