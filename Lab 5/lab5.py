# Nicholas Garth 101227727
import math

# Define Functions
# Exercise 1 Fuction
def area_cylinder(radius: float, height: float) -> float:
    '''Calculates the area of a cylinder given the radius and height'''
    return (2 * math.pi * height) + (2 * math.pi * pow(radius, 2))

# Exercise 2 Functions
def accrued_amount(P: float, r: float, t: float) -> float: 
    '''Calculates the accrued amount given principle amount, rate of interest, and number of periods'''
    return P * pow((1 + r), t)
def principle_amount(A: float, r: float, t: float) -> float:
    '''Calculates the principle amount given accrued amount, rate of interest, and number of periods'''
    return A / pow((1 + r), t)
def rate_interest(A: float, P: float, t: float) -> float:
    '''Calculates the rate of interest given accrued amount, principle amount, and number of periods'''
    return ((pow((A / P), (1/t))) - 1) * 100
def number_period(A: float, P: float, r: float) -> float:
    '''Calculates the number of periods given accrued amount, principle amount, and rate of interest'''
    return (math.log((A / P))) / (math.log((1+r)))


# Exercise 1
print("Exercise one has begun (:") # Print statment saying the exercise has begun.

# Calculate the area and assign it to variable 
cylinderArea = area_cylinder(6, 7)

# Print statement and result to pyhton shell
print("The area of a cylinder with a radius of 6 and a height of 7 is:", cylinderArea)


# Exercise 2
print("\nExercise two has begun :)") # Print statment saying the exercise has begun.

# Ask user what they want to calculate
userChoice = int(input("What do you want to calculate? \n1) Accrued Amount\n2) Principle Amount\n3) Rate of Interest\n4) Number of Periods\nEnter the number associated with the option: "))


# Determine what code should be executed based on the users selection
if userChoice == 1: # Accrued Amount
    # Print statement saying what selection was chosen
    print("\nAccrued Amount calculator has begun!")
    
    # Define Variables
    P = float(input("Enter the Principle Amount: $"))
    r = float(input("Enter the rate of interest per period: %"))
    t = int(input("Enter the number of periods: "))

    # Convert rate (r) from percentage to decimal
    r = r/100

    # Calculate the Accrued Amount
    accruedAmount = accrued_amount(P, r, t)

    # Print statement and result to python shell
    print("Your accrued amount is:", '${:.2f}'.format(accruedAmount))
elif userChoice == 2: # Principle Amount
    # Print statement saying what selection was chosen
    print("\nPrinciple Amount calculator has begun!")
    
    # Define Variables
    A = float(input("Enter the Accrued Amount: $"))
    r = float(input("Enter the rate of interest per period: %"))
    t = int(input("Enter the number of periods: "))

    # Convert rate (r) from percentage to decimal
    r = r/100

    # Calculate the Principle Amount
    principleAmount = principle_amount(A, r, t)
    
    # Print statement and result to python shell
    print("Your principle amount is:", '${:.2f}'.format(principleAmount))
elif userChoice == 3: # Rate Of Interest
    # Print statement saying what selection was chosen
    print("\nRate Of Interest calculator has begun!")
    
    # Define Variables
    A = float(input("Enter the Accrued Amount: $"))
    P = float(input("Enter the Principle Amount: $"))
    t = int(input("Enter the number of periods: "))
    
    # Calculate the Rate of Interest
    rateOfInterest = rate_interest(A, P, t)
    
    # Print statement and result to python shell
    print("Your rate of interest is:", '{:.4}%'.format(rateOfInterest))
elif userChoice == 4: # Number Of Periods
    # Print statement saying what selection was chosen
    print("\nNumber of Periods calculator has begun!")
    
    # Define Variables
    A = float(input("Enter the Accrued Amount: $"))
    P = float(input("Enter the Principle Amount: $"))
    r = float(input("Enter the rate of interest per period: %"))

    # Convert rate (r) from percentage to decimal
    r = r/100

    # Calculate the Number of Periods
    numberOfPeriods = number_period(A, P, r)

    # Print statement and result to python shell
    print("Your number of periods is:", '{:.2f}'.format(numberOfPeriods))
