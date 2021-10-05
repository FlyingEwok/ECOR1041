# Nicholas Garth 101227727

# Exercise 1 Functions
def test_int(test: int, x: int) -> int:
    """Tests if a value is equal to another value"""
    # Introduce global variables into function
    global counterPassed
    global counterFailed
    
    # Body
    if not test == x:
        print("Test Failed")
        counterFailed += 1
    else:
        print("Test passed")
        counterPassed += 1
def factorial(n: int) -> int:  
    """Return n! for positive values of n.  
  
    >>> factorial(1)  
    1  
    >>> factorial(2)  
    2  
    >>> factorial(3)  
    6  
    >>> factorial(4)  
    24  
    """      
    fact = 1      
    for i in range(2,n+1):  
        fact = fact * n  
     
    return fact
# Exercise 2 Function
def triangleType(a: int, b: int, c: int) -> str:
    """Return triangle type given the sides"""
    if a == b == c:
        return "Equilateral"
    elif a == b != c or a == c != b or c == b != a:
        return "Isosceles"
    else:
        return "Scalene"
# Exercise 3 Functions
def discountPercentage(price: float) -> float:
    """Return discount percentage for given price"""
    if price < 10:
        return 0
    elif price <= 65:
        return 0.09
    elif price <= 120:
        return 0.13
    elif price <= 200:
        return 0.17
    elif price > 200:
        return 0.20
def discount(price: float) -> float:
    """Returns discounted price"""
    # Calculate the discount percentage
    itemDiscountPercentage = discountPercentage(price)
    # Calculate discount
    itemDiscount = price * itemDiscountPercentage
    # Return final price
    return price - itemDiscount

# Exercise 1
print("Exercise 1 has begun:")

# Define the variables containing the returned factorials
factorialTest1 = factorial(1)
factorialTest2 = factorial(2)
factorialTest3 = factorial(3)
factorialTest4 = factorial(4)

# Define counter variables
counterPassed = 0
counterFailed = 0

# Factorial(1) Testing
print("\nTesting factorial(1)")
print("Expected result: 1, Actual result:", factorialTest1) # Print expected results vs the Actual result
test_int(factorialTest1, 1) # Call the test function

# Factorial(2) Testing
print("\nTesting factorial(2)")
print("Expected result: 2, Actual result:", factorialTest2) # Print expected results vs the Actual result
test_int(factorialTest2, 2) # Call the test function

# Factorial(3) Testing
print("\nTesting factorial(3)")
print("Expected result: 6, Actual result:", factorialTest3) # Print expected results vs the Actual result
test_int(factorialTest3, 6) # Call the test function

# Factorial(4) Testing
print("\nTesting factorial(4)")
print("Expected result: 24, Actual result:", factorialTest4)
test_int(factorialTest4, 24)

# Print Failed & Passed Stats
print("\n",counterPassed, " tests passed for Exercise 1", sep = "")
print(counterFailed, "tests failed for Exercise 1")


# Exercise 2
print("\nExercise 2 has begun:")

# Have the user input values to form a triangle and assign to variable
testTriangle = triangleType(int(input("Enter a value for side 'a' of the triangle: ")), int(input("Enter a value for side 'b' of the triangle: ")), int(input("Enter a value for side 'c' of the triangle: ")))

# Print the triangle type
print(testTriangle, "is the type of triangle you've entered.")


# Exercise 3
print("\nExercise 3 has begun:")

# Have the user enter a price
itemPrice = float(input("Enter the price of the item to calculate the discounted price: $"))

# Call the function to calculate final price after discount
discountedPrice = discount(itemPrice)

# Print final statement
print("The item costs ", '${:.2f}'.format(itemPrice), ", with a discount of ", '{:.0f}%'.format(((discountPercentage(itemPrice)) * 100)), ", which makes your final price ", '${:.2f}'.format(discountedPrice), sep = "")