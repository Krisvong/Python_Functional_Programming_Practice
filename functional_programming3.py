#3 Write a function treemap() to map a function over nested list.
# >>> treemap(lambda x: x*x, [1, 2, [3, 4, [5]]]) [1, 4, [9, 16, [25]]]
# Hint: Using recursion may make this function easier to code. Don't forget to check the type of the element you are iterating over.

def treemap(f, lst):
    """Maps a function 'f' over a nested list '1st'. """

    result = [] # Create an empty list to store the mapped values

    for item in lst: # Iterate over each item in the list
        if isinstance(item, list):
            # If the item is a list, recursively call treemap on that list and append the result to the result list
            result.append(treemap(f, item))
        else:
            # If the item is not a list, apply the function 'f' to it and append the result to the result list
            result.append(f(item))


    return result # Return the mapped list

#test 

print(treemap(lambda i: i*i, [1, 2, [3, 4, [5]]]))