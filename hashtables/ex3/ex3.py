def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # need a dict
    mydict = {}
    
    # need a counter
    # run through the grid and and to dictionary
    for row in arrays:
        for col in row:
            if col not in mydict:
                mydict[col] = 0
            mydict[col] += 1

    length = (len(arrays))
    # tuple objects in dict
    # filter using comprehension on values
    new_dict = {key:value for (key,value) in mydict.items() if value == length}
    # convert to list
    result = list(new_dict.keys())
    
    return result



if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
