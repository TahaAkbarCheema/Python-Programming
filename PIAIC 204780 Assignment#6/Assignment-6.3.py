# ----------------------------------- Assignment # 6 --------------------------------------------

# NAME : Taaha Akbar Cheema
# ROLL NO:  PIAIC 204780
# Batch No : 70

 #--------------------------------Project 3: Student Report Card Generator--------------------
# Function to calculate grade based on average
def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

# Function to input student data and generate report card
def generate_report_card():
    students = {}  # Dictionary to store student data

    while True:
        # Input student details
        name = input("Enter student name (or type 'exit' to stop): ").strip()
        if name.lower() == 'exit':
            break

        roll_no = input(f"Enter roll number for {name}: ").strip()
        marks = []

        # Input marks for 5 subjects
        for i in range(1, 6):
            while True:
                try:
                    mark = float(input(f"Enter marks for Subject {i}: "))
                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break
                    else:
                        print("Marks should be between 0 and 100. Please enter again.")
                except ValueError:
                    print("Invalid input! Please enter a numeric value.")
        
        # Calculate total, average, and grade
        total = sum(marks)
        average = total / len(marks)
        grade = calculate_grade(average)

        # Store the student data
        students[name] = {
            "roll": roll_no,
            "marks": marks,
            "total": total,
            "average": average,
            "grade": grade
        }

        # Display the report card
        print("\n--- Report Card ---")
        print(f"Student Name: {name}")
        print(f"Roll No: {roll_no}")
        print(f"Marks: {marks}")
        print(f"Total: {total}")
        print(f"Average: {average:.2f}")
        print(f"Grade: {grade}")
        print("\n")

    # Display summary of all students (if any)
    if students:
        print("\n--- All Student Report Cards ---")
        for name, details in students.items():
            print(f"Student Name: {name}")
            print(f"Roll No: {details['roll']}")
            print(f"Marks: {details['marks']}")
            print(f"Total: {details['total']}")
            print(f"Average: {details['average']:.2f}")
            print(f"Grade: {details['grade']}")
            print("-" * 30)
    else:
        print("No student data to display.")

# Run the system
if __name__ == "__main__":
    generate_report_card()

