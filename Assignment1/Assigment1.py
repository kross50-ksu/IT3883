# Program Name: Assignment1.py
# Student Name: Khaliya Ross
# Assignment Number: Lab1
# Due Date: 06/12/2026
# Purpose: Create a text-based menu-driven program that allows the user to manage an input buffer.
# The program should allow the user to append data to the buffer, clear the buffer, display the buffer contents, and exit the program.
# Resources: - W3Schools Python Tutorial: https://www.w3schools.com/python/

# Function to display the menu and handle user input
def main():
    buffer = ""
# While loop to continuously display the menu until the user chooses to exit
    while True:
        # Display the menu options
        print("\nMenu:")
        print("\nPlease choose an option:")
        print("---------------------------------")
        print("1. Append data to the input buffer")
        print("2. Clear the input buffer")
        print("3. Display the input buffer")
        print("4. Exit the program")
        print("")
# Handle the user's choice 1- append data, 2- clear buffer, 3- display buffer, 4- exit program
        choice = input("Enter your choice (1-4): ")
# Append data to the buffer if the user chooses option 1
        if choice == "1":
            new_text = input("\nEnter text to append: ")
            buffer += new_text + "\n"
            print(f"\n'{new_text}' has been appended to the input buffer.")
# Clear the buffer if the user chooses option 2
        elif choice == "2":
            buffer = ""
            print("\nInput buffer has been cleared.")
# Display the current contents of the buffer if the user chooses option 3
        elif choice == "3":
            print("\nCurrent buffer contents:")
            print(buffer)
# Exit the program if the user chooses option 4
        elif choice == "4":
            print("\nExiting program.")
            break
# Handle invalid input 
        else:
            print("\nInvalid choice. Please enter a number from 1 to 4.")
# Call the main function to start the program
if __name__ == "__main__":
    main()