#!/usr/bin/env python3

# Created by: Dylan Hanna
# Created on: October 2019
# This tells you if you can date the ladies grandchild


def main():
    while True:
        try:
            age = int(input("Please enter your age: "))

            if age >= 25 and age <= 40:
                print()
                print("You may date my grandchild")

            else:
                print()
                print("You may not date my grandchild")

        except ValueError:
            print()
            print("That is not your age")
            print()
            continue

        else:
            break


if __name__ == "__main__":
    main()