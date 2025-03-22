def calculate_grade(percentage):
    """Returns a grade based on percentage."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

def main():
    """Main function to get student marks and display results."""
    student_name = input("Enter student name: ")
    num_subjects = int(input("Enter number of subjects: "))

    marks = []
    for i in range(num_subjects):
        mark = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)

    total_marks = sum(marks)
    percentage = total_marks / num_subjects
    grade = calculate_grade(percentage)

    print("\n--- Student Report ---")
    print(f"Name: {student_name}")
    print(f"Total Marks: {total_marks}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
