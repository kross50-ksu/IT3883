# Program Name: Assignment2.py
# Student Name: Khaliya Ross
# Assignment Number: Lab2
# Due Date: 06/19/2026
# Purpose: This program reads student names and six test scores from an input file, calculates each 
# student's final average, and prints the results in descending order by average grade.
# Resources: - W3Schools Python Tutorial: https://www.w3schools.com/python/

# Function to read student data from a file, calculate averages, and display results
def main():
    file_name = 'Assignment2\\Assignment2input.txt'

    # Create an empty list to store student data
    student_averages = []

    # Open and read the file
    with open(file_name, "r") as infile:
        for line in infile:
            # Remove extra spaces/newlines and split the line into parts
            parts = line.strip().split()

            # First item is the student's name
            student_name = parts[0]

            # The remaining 6 items are scores
            scores = []
            for value in parts[1:]:
                scores.append(float(value))

            # Calculate the average of the 6 scores
            average = sum(scores) / len(scores)

            # Store the name and average as a tuple
            student_averages.append((student_name, average))

    # Sort students by average in descending order
    student_averages.sort(key=lambda student: student[1], reverse=True)

    # Print the results
    for student in student_averages:
        print(student[0], format(student[1], ".2f"))

# Call the main function to start the program
if __name__ == "__main__":
    main()