# Program Name: FE_CoinConverter.py
# Course: IT3883 / Section W02
# Student Name: Khaliya Ross
# Assignment Number: Sprint 1 – Coin Converter Program
# Due Date: 07/27/2026
# Purpose: Interprets pseudo-English statements describing quantities of coins and converts each 
# coin group into its monetary value, and outputs the total amount in dollars formatted to two decimal places.
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
    total = 0.0
    # Split by "and" to get each coin group
    parts = sentence.split("and")
    for part in parts:
        part = part.strip()
        tokens = part.split()
        # Expect: "<quantity> <denomination>"
        quantity = tokens[0]
        denomination = tokens[1].lower()
        if not quantity.isdigit():
            raise ValueError(f"Invalid quantity: {quantity}")
        if denomination not in COIN_VALUES:
            raise ValueError(f"Invalid coin type: {denomination}")
        total += int(quantity) * COIN_VALUES[denomination]
    return "$"+ f"{total:.2f}"

# Example manual test
if __name__ == "__main__":
    print(convert_sentence("1 penny and 2 nickels"))