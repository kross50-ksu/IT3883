# Program Name: Assignment1.py
# Student Name: Khaliya Ross
# Assignment Number: Lab1
# Due Date: 06/12/2026
# Purpose: Create a text-based menu-driven program that allows the user to manage an input buffer.
# The program should allow the user to append data to the buffer, clear the buffer, display the buffer contents, and exit the program.
# Resources: - W3Schools Python Tutorial: https://www.w3schools.com/python/

def main():
    buffer = ""

    while True:
        print("\nMenu:")
        print("\nPlease choose an option:")
        print("---------------------------------")
        print("1. Append data to the input buffer")
        print("2. Clear the input buffer")
        print("3. Display the input buffer")
        print("4. Exit the program")
        print("")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            new_text = input("\nEnter text to append: ")
            buffer += new_text + "\n"
            print(f"\n'{new_text}' has been appended to the input buffer.")

        elif choice == "2":
            buffer = ""
            print("\nInput buffer has been cleared.")

        elif choice == "3":
            print("\nCurrent buffer contents:")
            print(buffer)

        elif choice == "4":
            print("\nExiting program.")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()