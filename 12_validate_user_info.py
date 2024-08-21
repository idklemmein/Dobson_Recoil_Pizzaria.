
# function to validate users name (no digits allowed)
def validate_name(question):
    while True:
        response = input(question).strip()
        if response == "":
            print("Sorry, this field cannot be blank")
        elif all(letters.isalpha() or letters.isspace() for letters in response):
            return response
        else:
            print("Invalid input. Please enter letters only.")

# Test
if __name__ == "__main__":
    name = validate_name("Please enter your name: ")
    print(f"Name entered: {name}")


# function to validate users phone number (max 14 digits)
def validate_phone(question):
    while True:
        response = input(question).strip()
        if response.isdigit() and len(response) <= 14:
            return response
        else:
            print("Invalid input. Please enter digits only, with a maximum of 14 digits.")

# Test
if __name__ == "__main__":
    phone = validate_phone("Please enter your phone number (max 14 digits): ")
    print(f"Phone number entered: {phone}")

# user is asked for address if they pick delivery.
def validate_address(question):
    while True:
        response = input(question).strip()
        if response == "":
            print("Sorry, this field cannot be blank.")
        elif all(char.isalnum() or char.isspace() for char in response):
            return response
        else:
            print("Invalid input. Please enter letters, numbers, and spaces only.")

# Test
if __name__ == "__main__":
    address = validate_address("Please enter your address: ")
    print(f"Address entered: {address}")