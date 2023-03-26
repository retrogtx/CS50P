with open("names.txt") as file:
    for line in sorted(file, reverse=True):
        print("Hello,", line.rstrip())
