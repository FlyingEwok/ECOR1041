# Nicholas Garth 101227727


# Exercise 1 functions
def ticket_price(age: int, weekend: bool) -> float:
    """Returns ticket price after applying applicable discounts"""
    # Determine the base price if its a weekend or weekday
    if weekend:
        baseTicketPrice = 30.00 # weekend price
    else:
        baseTicketPrice = 40.00 # weekday price
    
    # Determine if person is eligable for a senior discount
    if age >= 65:
        return baseTicketPrice * 0.50 # Return ticket price with 50% discount
    else:
        return baseTicketPrice
def weekend(day: str) -> bool:
    """Returns boolean if its the weekend given the day of the week"""
    if day == "Saturday" or day == "saturday" or day == "Sunday" or day == "sunday":
        return True
    else:
        return False # This seems to be needed in order to return False, without this here it returns None

# Exercise 2 function
def suggested_activity(temp: int) -> str:
    '''Returns suggested activity given temperature'''
    if 80 <= temp < 95:  
        return 'Swimming'
    elif 60 <= temp < 80:
        return 'Tennis'
    elif 40 <= temp < 60:
        return 'Golf'
    elif 20 <= temp < 40:
        return 'Skiing'
    elif temp > 95 or temp < 20:
        return "Visit our shops!"

# Exercise 3 function
def great_42(a: int, b: int) -> bool:
    """Returns a true or false if 42 is either a, b, the sum, or the difference"""
    sum = a+b
    difference = a-b

    if a == 42 or b == 42 or sum == 42 or difference == 42:
        return True
    else:
        return False # This seems to be needed in order to return False, without this here it returns None

# Exercise 4 function
def sortIntegers(a: int, b: int, c: int) -> list:
    """Returns a list of intgers in decending order"""
    if a > b and b > c:
        return [c,b,a]
    elif b > c and c > a:
        return [a,c,b]
    elif c > a and a > b:
        return [b,a,c]

# Exercise 5 function
def unique_sum(a: int, b: int, c: int) -> int:
    """Returns the sum of all unique values"""
    if a == b:
        return c
    elif c == b:
        return a
    elif c == a:
        return b
    else:
        return a+b+c

# Exercise 1
print("Exercise 1 has begun: ") # Print Exercise has begun

# Define variables
age = int(input("Enter your age: "))
day = str(input("Enter the day of the week you want to go: "))

# Print final answer
print('${:.2f}'.format(ticket_price(age, weekend(day))))

# Exercise 2
print("\nExercise 2 has begun: ") # Print Exercise has begun

temp = int(input("What is the temperature out in ℉? "))

print("The suggested activity to do is: ", suggested_activity(temp))

# Exercise 3
print("\nExercise 3 has begun: ") # Print Exercise has begun

print("It's", great_42(abs(int(input("Enter a intger for a: "))), abs(int(input("Enter a integer for b: ")))), " that 42 is either a sum, difference, or is one of the values")

# Exercise 4
print("\nExercise 4 has begun: ") # Print Exercise has begun

# Print the decending order of values entered by user
print("The decending order of the integers you entered is: ", sortIntegers(int(input("Enter a integer: ")), int(input("Enter another integer: ")), int(input("Enter another integer: "))))

# Exercise 5
print("\nExercise 5 has begun: ") # Print Exercise has begun

# Prints the unique sum
print("The unique sum is: ", unique_sum(int(input("Enter a integer: ")), int(input("Enter another integer: ")), int(input("Enter another integer: "))))