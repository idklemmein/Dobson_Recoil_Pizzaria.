# this code is used as an I. D checker for both the toppings menu and pizza menu. It checks if the user
# has entered any number from 1-10 and it will not accept any other number
def num_check(question, low, high):
    error = f" Error! Please enter a number between {low} and {high}"
    while True:
        to_check = input(question)
        if to_check == "xxx":
            return to_check
        try:
            response = int(to_check)
            if response >= low and response <= high:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

# Test
if __name__ == "__main__":
    number = num_check("Enter a number between 1 and 10 or xxx to finish: ", 1, 10)
    print(f"You entered: {number}")