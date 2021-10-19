# Nicholas Garth 101227727

def count_odds(list: list) -> list:
    """Returns a list with only odd value from given list

    >>> count_odds([1,2,3,4,5])
    [1, 3, 5]
    >>> count_odds([0, -1, -2, -3, 3, 9, 10])
    """
    oddList = []
    for i in list:
        if (i%2 == 1): # Check if i is odd
            oddList = oddList + [i]
    return oddList
def Fibonacci_sequence(n: int) -> list:
    """Returns Fibonacci sequence up to nth term

    >>> Fibonacci_sequence(7)
    [0, 1, 1, 2, 3, 5, 8]
    >>> Fibonacci_sequence(21)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    >>> Fibonacci_sequence(-3)
    []
    >>> Fibonacci_sequence(0)
    []
    """
    fibonacciList = []
    count = 0
    n1, n2 = 0, 1
    while count < n:
       fibonacciList = fibonacciList + [n1]
       nth = n1 + n2
       # update values till the nth term
       n1 = n2
       n2 = nth
       count += 1
    return fibonacciList
def unique_list(list: list) -> list:
    """Returns a unique list given a non unique list

    >>> unique_list(['cat', 'dog', 'cat', 'bug', 'dog', 'ant', 'dog', 'bug'])
    ['cat', 'dog', 'bug', 'ant']
    >>> unique_list(['penny', 'dime', 'penny', 'quarter', 'dime', 'nickle', 'quarter'])
    ['penny', 'dime', 'quarter', 'nickle']
    """
    uniqueList = []
    for i in list:
        if (i not in uniqueList):
            uniqueList = uniqueList + [i]
    return uniqueList
def max_min(list: list) -> str:
    """Returns a string stating the largest and smallest value in a list
    
    >>> max_min([1,2,3,4,5])
    max =5 and min =1
    >>> max_min([0, -1, -2, -3, 3, 9, 10])
    max =10 and min =-3
    """
    min = list[0]
    max = list[0]
    for i in list:
        if i > max:
            max = i
        elif i < min:
            min = i
    return 'max =' + str(max) + ' and ' + 'min =' + str(min)
def max_occurrences(list: int) -> int:
    """Returns the value that occurs the most in given list

    >>> max_occurrences([2, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2])
    2
    >>> max_occurrences([5, 5, 5, 5, 9, 6, 9, 9, 5, 9, 9, 5])
    5
    """
    counter = 0
    num = list[0]
    
    for i in list:
        occurence = list.count(i)
        if (occurence > counter):
            counter = occurence
            num = i
    return num
def sum_range(list: list, m: int, n: int) -> int:
    """Returns the sum of a given range from a given list

    >>> sum_range([2, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2], 4,9)
    28
    >>> sum_range([5, 5, 5, 5, 9, 6, 9, 9, 5, 9, 9, 5], 0, 5)
    35
    """
    sum = 0
    for i in range(m,n+1,1):
        sum += list[i]
    return sum
def bank_statement(list: list) -> list:
    """Returns a list with the deposited amount, withdrawed amount, and total amount
    >>> bank_statement([1000, -500, 250, -1200])
    [1250, -1700, -450]
    >>> bank_statement([5000, -600, 10, -2000])
    """
    depositAmt = 0
    withdrawlAmt = 0
    totalAmt = 0
    for i in list:
        if i >= 0:
            depositAmt += i
        else:
            withdrawlAmt += i * -1
        totalAmt += i
    return [depositAmt, withdrawlAmt * -1, totalAmt]      
def prime_numbers(l: int, u: int) -> list:
    """Returns a list with all prime number in between given range

    >>> prime_numbers(1, 4)
    [1, 2, 3]
    >>> prime_numbers(250, 350)
    [251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349]
    """
    primeList = []
    for num in range(l,u):
        if num >= 1:
            for i in range(2, num): # Check if num is prime
                if (num % i) == 0:
                    break
            else:
                primeList = primeList + [num] # Add num to list
    return primeList
def reverse(list: list) -> list:
    """Returns a list reversed of given list

    >>> reverse([1,2,3,4,5])
    [5, 4, 3, 2, 1]
    >>> reverse([2, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2])
    [2, 1, 9, 6, 4, 3, 2, 1, 6, 1, 5, 6, 2, 8, 9, 7, 4, 2]
    """
    for i in range(len(list)-1, -1, -1):
        yield list[i]

# Exercise 1
print("Exercise 1 has begun:")

# Define Lists
list1 = [1,2,3,4,5]
list2 = [0, -1, -2, -3, 3, 9, 10]
oddList1 = count_odds(list1)
oddList2 = count_odds(list2)

# Print odd lists
print(oddList1, "\n", oddList2, sep = "")

# Exercise 2
print("\nExercise 2 has begun:")

# Print test cases
print(Fibonacci_sequence(7), "\n", Fibonacci_sequence(21), "\n", Fibonacci_sequence(-3), "\n", Fibonacci_sequence(0), sep = "")

# Exercise 3
print("\nExercise 3 has begun:")

# Create lists
animalList = ['cat', 'dog', 'cat', 'bug', 'dog', 'ant', 'dog', 'bug']
coinList = ['penny', 'dime', 'penny', 'quarter', 'dime', 'nickle', 'quarter']

# Print Test Cases
print(unique_list(animalList), "\n", unique_list(coinList), sep="")

# Exercise 4
print("\nExercise 4 has begun:")

# Print test cases using lists from exercise 1
print(max_min(list1), "\n", max_min(list2), sep="")

# Exercise 5
print("\nExercise 5 has begun:")

# Define lists
list3 = [2, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
list4 = [5, 5, 5, 5, 9, 6, 9, 9, 5, 9, 9, 5]

# Print test cases
print(max_occurrences(list3), "\n", max_occurrences(list4), sep="")

# Exercise 6
print("\nExercise 6 has begun:")

# Print test cases using lists from exercise 5
print(sum_range(list3,4,9), "\n", sum_range(list4,0,5), sep="")

# Exercise 7
print("\nExercise 7 has begun:")

print(bank_statement([1000, -500, 250, -1200]), "\n", bank_statement([5000, -600, 10, -2000]), sep="")

# Exercise 8
print("\nExercise 8 has begun:")

# Print prime lists
print(prime_numbers(1, 4), "\n", prime_numbers(250, 350), sep="")

# Exercise 9
print("\nExercise 9 has begun:")

# Print reversed list using lists from exercise 1 and 5
print(list(reverse(list1)), "\n", list(reverse(list3)), sep="")