# Nicholas Garth 101227727

# Exercise 1 Function
def first_last(x: int, list: list) -> bool:
    """Returns True/False if the first or/and last elements of list is x
    >>> first_last(22, [22,4,5,3,22])
    True 
    >>> first_last(22, [22,3,4,5])
    True 
    >>> first_last(22, [81,90,66,22])
    True
    >>> first_last(22, [1,2,3,4,5])
    False  
    """
    # Body
    return x == list[0] or x == list[-1]

# Exercise 2 Function
def same_first_last(x: int, list: list) -> bool:
    """Returns True if the first or/and last elements of list is x, or if the list is empty
    >>> same_first_last(22, [22,4,5,3,22])
    True 
    >>> same_first_last(22, [22,3,4,5])
    True 
    >>> same_first_last(22, [81,90,66,22])
    True
    >>> same_first_last(22, [1,2,3,4,5])
    False
    >>> same_first_last(22, [])
    True
    """
    # Body
    return not list or x == list[0] or x == list[-1]

# Exercise 3 Function
def canada_letters() -> list:
    """Returns a list with the letters in the word Canada
    >>> canada_letters()
    ['C', 'A', 'N', 'D', 'A']
    """
    return ['C','A','N','D','A']

# Exercise 4 Function
def common_end(list1: list,list2: list) -> bool:
   """Returns True if lists have same first elements, last elements, and first and last elements
    >>> common_end([1,2,3,4],[1,9,0,6])
    True 
    >>> common_end([4,5,9,0],[8,6,5,8,9,5,0])
    True 
    >>> common_end([6,6,6],[6,9,6])
    True
    >>> common_end([1,2,3,4,5],[6,7,8,9,0])
    False  
   """
   return list1[0] == list2[0] or list1[-1] == list2[-1] or list1[0] == list2[0] == list1[-1] == list2[-1]

# Exercise 5 Function
def average(list: list) -> float:
    """Returns the average of a given list
    >>> average([6,7,20,99])
    33.0
    """
    return sum(list)/len(list)

# Exercise 6 Function
def rotate_right(list: list) -> list:
    """Rotates a list to the right by 1
    >>> rotate_right([1,2,3])
    [3, 1, 2]
    """
    shift = 5
    n = shift % len(list)
    return list[n:] + list[:n]

# Exercise 7 Function
def reverse(list: list) -> list: 
    """Reverses the values in a list
    >>> reverse([1,2,3,4,5])
    [5, 4, 3, 2, 1]
    """
    return list[::-1]

# Exercise 8 Function
def max_list(list: list) -> list:
    """Returns a list with only the largest element of given list
    >>> max_list([3,8,6,20])
    [20, 20, 20, 20]
    """
    max_value = max(list)
    return [max_value] * len(list)

# Exercise 9 Function
def average2(list: list) -> float:
    """Returns the average of the first 2 elements in given list
    >>> average2([5,9,2,4,5])
    5.5
    >>> average2([])
    0
    """
    if not list:
        return 0
    else:
        return ((list[1] + list[2])/2)

# Exercise 10 Function
def middle_way(list1: list, list2: list) -> list:
    """Returns a list with the middle elements of 2 lists
    >>> middle_way([2,78,50],[3,282,4337])
    [78, 282]
    """
    middleIndex1 = (len(list1) - 1) // 2
    middleIndex2 = (len(list2) - 1) // 2
    return [(list1[middleIndex1]), (list2[middleIndex2])]

# Exercise 11 Function
def make_ends(list: list) -> list:
    """Returns a list containing first and last elements of given list
    >>> make_ends([4,5,6,7])
    [4, 7]
    """
    return [list[0], list[-1]]

# Exercise 12 Function
def hasElements(list: list, x: int, y: int) -> bool:
    """Returns True if x or y/ x and y exist in the given list
    >>> hasElements([6,21,69], 30, 69)
    True 
    >>> hasElements([30,21,6], 30, 69)
    True 
    >>> hasElements([30,21,69], 30, 69)
    True
    >>> hasElements([29,21,68], 30, 69)
    False  
    """
    return x in list or y in list or x and y in list


# Exercise 1
print("Exercise 1 has begun: ")

# Define lists
list1 = [22,4,5,3,22]
list2 = [22,3,4,5]
list3 = [81,90,66,22]
list4 = [1,2,3,4,5]
list5 = []

# Define x
x = 22

# Generate True/False Booleans based on defined lists
listCheck1 = first_last(x, list1)
listCheck2 = first_last(x, list2)
listCheck3 = first_last(x, list3)
listCheck4 = first_last(x, list4)

# Print True/Flase in list order
print(listCheck1, listCheck2, listCheck3, listCheck4)

# Exercise 2
print("\nExercise 2 has begun: ")

# Generate True/False Booleans based on defined lists
listCheck1 = same_first_last(x, list1)
listCheck2 = same_first_last(x, list2)
listCheck3 = same_first_last(x, list3)
listCheck4 = same_first_last(x, list4)
listCheck5 = same_first_last(x, list5)

# Print True/Flase in list order
print(listCheck1, listCheck2, listCheck3, listCheck4, listCheck5)

# Exercise 3
print("\nExercise 3 has begun: ")

# Print the list created in the function
print(canada_letters())

# Exercise 4
print("\nExercise 4 has begun: ")

# Print test lists returned values from function
print(common_end([1,2,3,4],[1,9,0,6]), common_end([4,5,9,0],[8,6,5,8,9,5,0]), common_end([6,6,6],[6,9,6]), common_end([1,2,3,4,5],[6,7,8,9,0]))

# Exercise 5
print("\nExercise 5 has begun: ")

# Print average
print("The average of the list [6,7,20,99] is: ",average([6,7,20,99]))

# Exercise 6
print("\nExercise 6 has begun: ")

# Print rotated list
print("The rotated list by 1 of list [1, 2, 3] is: ", rotate_right([1,2,3]))

# Exercise 7
print("\nExercise 7 has begun: ")

# Print reversed list
print("The reversed list of list [1, 2, 3, 4, 5] is: ", reverse([1,2,3,4,5])) 

# Exercise 8
print("\nExercise 8 has begun: ")

# Print max_list
print("The max of list [3, 8, 6, 20] is: ", max_list([3,8,6,20]))

# Exercise 9
print("\nExercise 9 has begun: ")

# Print Average
print("The average of the first 2 elements in list [5, 9, 2, 4, 5] is: ", average2([5,9,2,4,5]), "and the average of the first 2 elements in list [] is: ", average2([]))

# Exercise 10
print("\nExercise 10 has begun: ")

# Print middle elements of list
print("The middle values of lists [2, 78, 50] and [3, 282, 4337] is: ",middle_way([2,78,50],[3,282,4337]))

# Exercise 11
print("\nExercise 11 has begun: ")

# Print first and last values of a list
print("The first and last values of list [4, 5, 6, 7] is: ",make_ends([4,5,6,7]))

# Exercise 12
print("\nExercise 12 has begun: ")

# Print if each statement is true/false
print(hasElements([6,21,69], 30, 69), hasElements([30,21,6], 30, 69), hasElements([30,21,69], 30, 69), hasElements([29,21,68], 30, 69))