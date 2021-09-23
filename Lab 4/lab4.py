#Nicholas Garth 101227727
import math 
 
# Define Functions
def area_of_disk(radius): 
    return math.pi * radius ** 2 
 
def area_of_ring(outer, inner): 
    return area_of_disk(outer) - area_of_disk(inner) 

def convert_to_litres_per_100_km(mpg):
    #Create variables for conversions
    LITRES_PER_GALLON = 4.54609
    KMS_PER_MILE = 1.60934

    if not mpg == 0:
        return 100 * LITRES_PER_GALLON / KMS_PER_MILE / mpg
    else:
        return print("You can't divide by zero!")

def mortgage_amount(principal, rate, n):
    if not rate == 0:
        return principal * ((rate * pow((1 + rate),n)) / (pow((1 + rate),n) - 1))
    else:
        print("You can't have a zero interest rate!")

def area_of_cone(height, radius):
    return (math.pi * pow(radius, 2)) + (math.pi * radius) * math.sqrt(pow(radius, 2) + pow(height, 2))

# Main Script
# Exercise 1

# Print Exercise 1 in terminal to seperate from other exercise
print("Starting Exercise 1:")

# Print the areas
area = area_of_disk(5)
print("Exercise 1: The area is:",area)

area = area_of_disk(5.0)
print("Exercise 1: The area is:",area)

area = area_of_ring(10, 5) 
print("Exercise 1: The area is:",area)

area = area_of_ring(10.0, 5.0)
print("Exercise 1: The area is:",area)

# Exercise 2

# Print Exercise 2 in terminal to seperate from other exercise
print("Starting Exercise 2:")

print("Exercise 2: 32 mpg =", convert_to_litres_per_100_km(32), "1/100 km")
print("Exercise 2: 0 mpg =", convert_to_litres_per_100_km(0), "1/100 km")
print("Exercise 2: The functions class is: ", type(convert_to_litres_per_100_km(32)), "\nWhich means it's working for a real number argument.")

# Exercise 3

# Print Exercise 3 in terminal to seperate from other exercise
print("Starting Exercise 3:")

# Ask the user to enter the values for principle, rate, and n
x = float(input ("Enter a principle loan amount: "))
y = float(input ("Enter a monthly rate of interest: "))
z = float(input("Enter the number of payments over the loan's lifetime: "))

mortgageAmount = mortgage_amount(x,y,z)

# Check if fuction did not end up returning none 
if not mortgageAmount == None:
    print("Exersise 3: The amount needed to be paid each month is: $",mortgageAmount)

# Exercise 4

# Print Exercise 4 in terminal to seperate from other exercise
print("Starting Exercise 4:")

# Ask the user for the height and radius of the cone. (Asking user to allow for any numbers to work)
height = float(input("Enter the height of the cone in cm: "))
radius = float(input("Enter the radius of the cone in cm: "))

# Print the outcome of the fuction with the values given by the user.
print("The area of the cone is: ", area_of_cone(height,radius),"cm squared")





