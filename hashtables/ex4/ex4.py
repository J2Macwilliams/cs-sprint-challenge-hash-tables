def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # create dict
    mydict={}
    # create result
    result = []
    # populate dict
    for i in range(len(a)):
        #  filter out negatives
        if a[i] < 0:
            # change to positive
            mydict[abs(a[i])] = i
    # list my dict
    keylist = list(mydict.keys())
    # compare and append
    for item in a:
        if item in keylist:
            result.append(item)
    
    return result

    

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
