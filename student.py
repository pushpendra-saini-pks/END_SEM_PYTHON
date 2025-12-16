import sys

class Student:
    def __init__(self, roll, name, fee, cgpa):
        self.roll = roll
        self.name = name
        self.fee = fee
        self.cgpa = cgpa

    def to_string(self):
        return f"{self.roll},{self.name},{self.fee},{self.cgpa}\n"


def update_file(filename):
    print(f"\nReopening file: {filename}")

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        updated_lines = []

        for line in lines:
            roll, name, fee, cgpa = line.strip().split(",")
            fee = float(fee)
            cgpa = float(cgpa)

            # Condition check (without using class object)
            if fee < 5000 and cgpa > 8:
                print(f"Updating fee to 0 for Roll No {roll}")
                fee = 0

            updated_lines.append(f"{roll},{name},{fee},{cgpa}\n")

        with open(filename, "w") as file:
            file.writelines(updated_lines)

    except IOError:
        print(f"Error: Unable to process file {filename}")


def main():
    if len(sys.argv) != 3:
        print("Error: Please provide exactly two filenames.")
        print("Usage: python program.py even.txt odd.txt")
        sys.exit(1)

    even_file = sys.argv[1]
    odd_file = sys.argv[2]

    students = [
        Student(1, "Amit", 4500, 8.5),
        Student(2, "Neha", 6000, 7.8),
        Student(3, "Rahul", 3000, 9.1),
        Student(4, "Pooja", 2000, 8.8),
        Student(5, "Karan", 5500, 6.9)
    ]

    try:
        with open(even_file, "w") as ef, open(odd_file, "w") as of:
            for s in students:
                if s.roll % 2 == 0:
                    ef.write(s.to_string())
                else:
                    of.write(s.to_string())
    except IOError:
        print("Error: Unable to open output files.")
        sys.exit(1)

    print("\nInitial data written to files successfully.")

    update_file(even_file)
    update_file(odd_file)

    print("\nFinal content of files:\n")

    display_file(even_file)
    display_file(odd_file)


def display_file(filename):
    print(f"Contents of {filename}:")
    try:
        with open(filename, "r") as file:
            print(file.read())
    except IOError:
        print("Error reading file")


if __name__ == "__main__":
    main()

