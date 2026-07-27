# Program Name: FE_CoinConverter.py
# Course: IT3883 / Section W02
# Student Name: Khaliya Ross
# Assignment Number: Sprint 2 – Corrected Coin Converter Program
# Due Date: 07/27/2026
# Purpose: Improved version of the coin conversion program that supports flexible 
# pseudo-English input, including descriptive words, variable spacing, and uppercase/lowercase 
# denominations. Extracts numeric quantities, identifies coin types, converts values, and 
# outputs the total in dollars.
# Resources: Python documentation (string methods, dictionaries) and Course notes

COIN_VALUES = {
    "penny": 0.01,
    "pennies": 0.01,
    "nickel": 0.05,
    "nickels": 0.05,
    "dime": 0.10,
    "dimes": 0.10,
    "quarter": 0.25,
    "quarters": 0.25
}

def convert_sentence(sentence):
    # Running total of all coin values
    total = 0.0

    # Split the sentence into coin groups using "and"
    # Example: "21 shiny pennies and 17 dimes" → ["21 shiny pennies", "17 dimes"]
    parts = sentence.split("and")

    # Process each coin group individually
    for part in parts:
        # Remove leading/trailing spaces from each group
        part = part.strip()

        # Split the group into individual words
        # Example: "21 shiny pennies" → ["21", "shiny", "pennies"]
        tokens = part.split()

        # Extract quantity: find the first numeric token in the group
        quantity = None
        for token in tokens:
            # Check if the token is a digit (e.g., "21")
            if token.isdigit():
                quantity = int(token)
                break

        # If no numeric quantity was found, the input is invalid
        if quantity is None:
            raise ValueError("No numeric quantity found.")

        # Extract denomination: the last word in the group
        # Example: ["21", "shiny", "pennies"] → "pennies"
        denomination = tokens[-1].lower()

        # Validate that the denomination exists in our coin dictionary
        if denomination not in COIN_VALUES:
            raise ValueError(f"Invalid coin type: {denomination}")

        # Add the value of this coin group to the running total
        total += quantity * COIN_VALUES[denomination]

    # Return the final total formatted to two decimal places
    return f"{total:.2f}"

# Example manual test
if __name__ == "__main__":
    print(convert_sentence("21 shiny pennies and 3 old nickels"))