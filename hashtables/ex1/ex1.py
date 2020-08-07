def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weight_lookup = {}
    for i in range(len(weights)):
        if weights[i] not in weight_lookup:
            weight_lookup[weights[i]] = [i]
        else:
            weight_lookup[weights[i]].append(i)
    
    for w in weights:
        match = limit - w
        if match in weight_lookup:
            if weight_lookup[match] > weight_lookup[w]:
                return [weight_lookup[match][0], weight_lookup[w][0]]
            elif weight_lookup[match] < weight_lookup[w]:
                return [weight_lookup[w][0], weight_lookup[match][0]]
            else:
                return [weight_lookup[w][1], weight_lookup[w][0]]

    return None

weights_2 = [3, 4]
answer_2 = get_indices_of_item_weights(weights_2, 2, 7)
print(answer_2)