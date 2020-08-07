def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    number_count = {}
    result = []

    for i in arrays:
        for j in i:
            if j not in number_count:
                number_count[j] = 0
            number_count[j] += 1
    
    sorted_number_count = list(number_count.items())
    sorted_number_count.sort(key=lambda kv: kv[1], reverse=True)

    for number in sorted_number_count:
        if number[1] == len(arrays):
            result.append(number[0])
        else:
            break

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
