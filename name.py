import sys

# try:
#     print("Hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments.")

# Check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments.")

elif len(sys.argv) > 2:
    sys.exit("Too many arguments.")

# Print if everthing is right
print("Hello, my name is", sys.argv[1])
