def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # create a dict for holding on to weights
    my_dict = {}
    identified = []
    # keys will be the item, value will be the index
    for i in range(length):
        my_dict[weights[i]] = i

    print(my_dict)
    # work thru the list somehow to find the limit
    for weight in weights:
        found = limit - weight
        if found in my_dict.keys():
             identified.append(my_dict[found])
    if len(identified) > 0:
        return identified
    else:
        return None
    

weights_1 = [4, 4]
print(get_indices_of_item_weights(weights_1, 2, 8))

