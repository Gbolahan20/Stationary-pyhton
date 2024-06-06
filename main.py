# Stationery Store Manager

import os

class Stationery:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

def add_stationery():
    name = input("Enter stationery name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    stationery = Stationery(name, quantity, price)
    with open("stationery.txt", "a") as file:
        file.write(f"{stationery.name},{stationery.quantity},{stationery.price}\n")

def display_stationery():
    with open("stationery.txt", "r") as file:
        for line in file:
            name, quantity, price = line.strip().split(",")
            print(f"Name: {name}, Quantity: {quantity}, Price: {price}")

def update_quantity():
    name = input("Enter stationery name: ")
    quantity = int(input("Enter new quantity: "))
    with open("stationery.txt", "r") as file:
        lines = file.readlines()
    with open("stationery.txt", "w") as file:
        for line in lines:
            stationery_name, stationery_quantity, stationery_price = line.strip().split(",")
            if stationery_name == name:
                file.write(f"{stationery_name},{quantity},{stationery_price}\n")
            else:
                file.write(line)

def main():
    while True:
        print("1. Add Stationery\n2. Display Stationery\n3. Update Quantity\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_stationery()
        elif choice == "2":
            display_stationery()
        elif choice == "3":
            update_quantity()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

