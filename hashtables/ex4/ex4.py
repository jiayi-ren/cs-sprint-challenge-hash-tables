def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    pos = {}
    neg = {}
    result = []
    for n in a:
        if n > 0:
            if n not in pos:
                pos[n] = True
        if n < 0:
            if n not in neg:
                neg[n] = True
    
    for pos_num in list(pos.keys()):
        if -pos_num in neg:
            result.append(pos_num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
