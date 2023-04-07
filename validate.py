email = input("What is your email? ").strip()

username, domain = email.split("@")

if username and domain.endwith(".edu"):
    print("Valid")

else:
    print("Invalid")
