#1 Write a function flatten_dict() to flatten a nested dictionary by joining the keys with . character.
# >>> flatten_dict({'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}) {'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}
# Hint: You can assume that all dictionary keys will be of type string, and that nested dictionaries will only be nested one layer deep (a dictionary of dictionaries will not have another dictionary nested inside it).

def flatten_dict(d):
    """Flattens a nested dictionary.
    keys must be strings in all dictionaries for this to work.
    """

    result = dict() # Create an empty dictionary to store the flattened key-value pairs

    for i in d.keys(): # Iterate over each key in the input dictionary
        if type(d[i]) == dict: #If the value is a dictionary, it needs to be flattened
            for k, v in d[i].items(): # Iterate over the key-value pairs in the nested dictionary
                new_key = i + "." + k # Create the new flattened key by joining the original key and the nested key
                result[new_key] = v # Add the key_value pair to the flattened dictionary

        else:
            # If the value is not a dictionary, add the key-value pair directly to the result dictionary 
            result[i] = d[i]



    return result # Return the flattened dictionary     

#test
nested_dict = {'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}
flattened_dict = flatten_dict(nested_dict)
print(flattened_dict)
