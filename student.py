class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")  # type: ignore


def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)  # type: ignore
    return student


if __name__ == "__main__":
    main()


# Week 8 - 40
