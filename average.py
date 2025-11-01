# Program to calculate average marks of students
# Improvements:
# - configurable number of subjects
# - simple input validation (non-negative marks)
# - handles duplicate student names by appending an index

def get_int(prompt, min_val=None):
    while True:
        try:
            val = int(input(prompt))
            if min_val is not None and val < min_val:
                print(f"Please enter an integer >= {min_val}.")
                continue
            return val
        except ValueError:
            print("Invalid integer. Try again.")

def get_float(prompt, min_val=None):
    while True:
        try:
            val = float(input(prompt))
            if min_val is not None and val < min_val:
                print(f"Please enter a number >= {min_val}.")
                continue
            return val
        except ValueError:
            print("Invalid number. Try again.")

def main():
    students = {}   # Dictionary to store student names and marks

    n = get_int("Enter number of students: ", min_val=1)
    subjects = get_int("Enter number of subjects per student: ", min_val=1)

    for i in range(n):
        base_name = input(f"\nEnter name of student {i+1}: ").strip()
        # handle duplicate names
        name = base_name
        counter = 1
        while name in students:
            name = f"{base_name}_{counter}"
            counter += 1

        total = 0.0
        for j in range(subjects):
            mark = get_float(f"Enter marks for subject {j+1}: ", min_val=0.0)
            total += mark
        average = total / subjects
        students[name] = average

    print("\nStudent Averages:")
    for name, avg in students.items():
        print(f"{name}: {avg:.2f}")

    # Find top student
    if students:
        topper = max(students, key=students.get)
        print(f"\nTop student is {topper} with average {students[topper]:.2f}")

if __name__ == "__main__":
    main()
