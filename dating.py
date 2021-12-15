#!/usr/bin/env python3

# Created by: Logan Sweeney
# Created on: Dec. 15, 2021
# This program determines whether or not someone is illegible
# of dating a grandchild.


def main():

    # user's input of age and name
    user_input_name = str(input("Enter your name: "))
    user_input_age = input("Enter your age: ")
    print()

    # process & output with try catch
    try:
        # Changing the input to an integer
        user_input_age = int(user_input_age)
        if user_input_age >= 25 and user_input_age < 40:
            print("{}, you are allowed to date our grandchild."
                  .format(user_input_name))
        elif user_input_age < 25:
            print("{}, you are not allowed to date our grandchild. Too young!"
                  .format(user_input_name))
        else:
            print("{}, you are not allowed to date our grandchild. Too old!"
                  .format(user_input_name))
    except Exception:
        print("This isn't even a number...")
    finally:
        print()
        print("Thanks for trying though.")


if __name__ == "__main__":
    main()
