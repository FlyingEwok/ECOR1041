"""
ECOR 1041 Lab 6 Solution Template

Author and Student Number: Nicholas Garth 101227727

This file is to be used in conjunction with the detailed lab description for Lab 6
Use this file to enter your answers to the series of exercises you will complete.

==========

Exercise 1: Single or Double Quotes - Does it matter?

Example, "haven't" or '"Spam, spam, spam," he said.'

>>> type('Welcome To ECOR 1041')
# Type what you see: 
<class 'str'>

>>> type("Welcome To Carleton University")
# Type what you see: 
<class 'str'>

>>> 'Welcome'
# Type what you see: 
'Welcome'

>>> ""     (An empty string - type two quotes with no spaces between them.)


>>> '"Hello, Welcome to Canada" he said.'
# Type what you see: (Nested quotations)
'"Hello, Welcome to Canada" he said.'

>>> "I haven't solved the mystery" 
# Type what you see: (Nested apostrophe)
"I haven't solved the mystery"

>>> 'I haven't solved the mystery' 
# Type what you see: (Nested apostrophe)
SyntaxError: invalid syntax (Failed due to the ' in haven't double quotes is required in this scenario)

Concluding Questions: Generally, either double or single quotes works well but can you give a scenario where one is better than the other?
Double quotes work the best when you want to have an ' in a word within the string Ex. "They've taken their time", and you would use single quotes when you want double quotes in the string. Ex. 'He said "stop"'

==================

Exercise 2: What operations are permitted with values of type str?

When used with strings, + is the concatenation operator. 

>>> 'Welcome ' + 'to Canada'
# Type what you see: 
'Welcome to Canada'

When used with strings, * is the replication operator.

>>> "Hello!" * 3
# Type what you see: 
'Hello!Hello!Hello!'

>>> 3 * "Hello!"
# Type what you see: (Reflect: What does this say about order of operators?)
'Hello!Hello!Hello!' (The output is the same if no matter what side the operator is on from the string, it means it doesn't matter where you put the operator, on the left of string, or on the right of string)

>>> "Hello!" * 0
# Type what you see: 
''

>>> "Hello!" * -3
# Type what you see: 
''

There are other operators to try now: - and /

>>> "Hello" - "He"
# Type what you see: 
TypeError: unsupported operand type(s) for -: 'str' and 'str'

>>> 'Hello' / 3
# Type what you see: 
TypeError: unsupported operand type(s) for /: 'str' and 'int'

Concluding Questions: Do some tests with the operands you know on Python. What operators work with strings?  Does the order of operands matter?
(You need to consider the cases where both operands are string and when just one of them is a string)
You can only use the multiply (*) operand with a string and a integer, and you can only add strings with other strings. Any other operators do not work.
The order of the operand only matters with adding a string with a string, it must be in between the two strings. The order of the operand doesn't matter when multiplying a string with a integer.

=======================

Exercise 3 : Understand the string representation

Is  the string '123' the same as the integer 123? 

>>> '123' + 456
# Type what you see: 
TypeError: can only concatenate str (not "int") to str

>>> '123' + '456'
# Type what you see: 
'123456'

Concluding Question: When a string looks like a number, is it a number or a string?
It is a string and cannot be used as an intger/float. You can add the two strings as showen above but it's not adding them numerically.
Since those numbers are a string you can't add a integer to it.

=========
Last edited: September 13, 2021
"""

# Nicholas Garth 101227727

def concatenates (s1: str, s2: str) -> str: 
    """ Return a string that is the concatenated string of the two 
arguments. 
 
    >>> concatenates ('Hello, ', 'world') 
    'Hello, world' 
    >>> concatenates ('Welcome to ', 'Canada')
    'Welcome to Canada' 
    >>> concatenates ('ECOR', '1041') 
    'ECOR1041'
    >>> concatenates ('', '')
    
    """
    # Body
    return s1 + s2

def total_length(s1: str, s2: str) -> int: 
    """ Return the sum of the lengths of s1 and s2. 
 
    >>> total_length('yes', 'no') 
    5 
    >>> total_length('yes', '')
    3 
    >>> total_length('YES!!!!', 'Noooooo')
    14 
    """ 
    # Body
    return len(s1 + s2)

def replicate(s1: str, s2: str) -> str:
    """ Return a replica of the concatenation of s1 and s2
    
    >>> replicate('a', 'b') 
    abab
    >>> replicate('ab', 'c')
    abcabcabc
    >>> replicate('abdcefg', 'hijk ')
    abdcefghijk abdcefghijk abdcefghijk abdcefghijk abdcefghijk abdcefghijk abdcefghijk abdcefghijk abdcefghijk abdcefghijk abdcefghijk abdcefghijk
    """
    # Body
    stringLength = total_length(s1, s2)
    stringConcatenate = concatenates(s1, s2)
    # Return replicated
    return stringConcatenate * stringLength



# Exercise 4
print("Exercise 4 has begun!")
# Print Result
result = concatenates('Hello, ', 'world')
print(result)
result = concatenates ('Welcome to ', 'Canada')
print(result)
result = concatenates ('ECOR', '1041')
print(result)
result = concatenates ('', '')

# Exercise 5
print("\nExercise 5 has begun!")
# Print Result
result = total_length('yes', 'no')
print(result)
result = total_length('yes', '')
print(result)
result = total_length('YES!!!!', 'Noooooo')
print(result)

# Exercise 6
print("\nExercise 6 has begun!")
# Print Result
result = replicate('a', 'b')
print(result)
result = replicate('ab', 'c')
print(result)
result = replicate('abdcefg', 'hijk ') # The space counts as a charachter
print(result)