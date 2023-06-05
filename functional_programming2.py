#2 Write a function unflatten_dict() to do reverse of flatten_dict.
# >>> unflatten_dict({'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}) {'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}
# Hint: You can assume that the keys for the dictionary will all be of type string, and that you never need to create more than one layer of nested dictionary. It may be helpful to create an empty dictionary as the value for the outer key ('b' in this example), then fill it in iteratively as you find keys that belong to that dictionary.

def unflatten_dict(d):
    """Unflattens a nested dictionary. (reverses flatten-dict)
    keys must be strings in all dictionaries for this to work
    """

    result = dict() # Create an empty dictionary to store the unflattened key value pairs

    for i in d.keys(): # Iterate over each key in the input dictionary
        if "." in i: # If the key contains a '.', it indicates nesting
            # Split the key into two parts: the new key and the inner key
            new_key, sep, inner_key = i.partition(".")

            # Create the new key's dictionary if it's not yet created
            if new_key not in result.keys():
                result[new_key] = dict()

            # Add the value to the inner dictionary
            result[new_key][inner_key] = d[i]

        else:
            # If the key does not contain a '.', it is not nested
            # Add the key-value pair directly to the result dictionary 
            result[i] = d[i]



    return result # Return the unflattened dictionary



# Test 
input_dict = {'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}
output_dict = unflatten_dict(input_dict)
print(output_dict)
