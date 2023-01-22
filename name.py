import sys

# try:
#     print("Hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments.")

# Check for errors
if len(sys.argv) < 2:
    print("Too few arguments.")

elif len(sys.argv) > 2:
    print("Too many arguments.")

# Print if everthing is right
else:
    print("Hello, my name is", sys.argv[1])
