# Program Name: Assignment5.py
# Course: IT3883/Section W02
# Student Name: Khaliya Ross
# Assignment Number: Assignment 5
# Due Date: 07/17/2026
# Purpose:
# Creates a SQLite database, loads temperature, data from a file, stores the data in a table,
# and calculates average temperatures.
# Resources
# Python SQLite documentation
# Course notes

import sqlite3

# Create database connection
connection = sqlite3.connect("weather.db")

# Create cursor
cursor = connection.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS temperature_data (
    id INTEGER PRIMARY KEY,
    day_of_week TEXT,
    temperature_value REAL
)
""")

# Open input file
with open("Assignment5input.txt", "r") as file:

    for line in file:

        # Remove extra spaces/newlines
        line = line.strip()

        # Split day and temperature
        day, temp = line.split(",")

        # Insert row into table
        cursor.execute("""
        INSERT INTO temperature_data
        (day_of_week, temperature_value)
        VALUES (?, ?)
        """, (day, float(temp)))

# Save changes
connection.commit()

# Average Sunday temperature
cursor.execute("""
SELECT AVG(temperature_value)
FROM temperature_data
WHERE day_of_week='Sunday'
""")

sunday_average = cursor.fetchone()[0]

# Average Thursday temperature
cursor.execute("""
SELECT AVG(temperature_value)
FROM temperature_data
WHERE day_of_week='Thursday'
""")

thursday_average = cursor.fetchone()[0]

# Display results
print("Average Sunday Temperature:", sunday_average)
print("Average Thursday Temperature:", thursday_average)

# Close connection
connection.close()