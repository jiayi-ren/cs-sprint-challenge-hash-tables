# Your code here

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    queries_dict = {}
    result = []
    for q in queries:
        if q not in queries_dict:
            queries_dict[q] = True

    for f in files:
        last = f.rsplit("/", 1)[-1]
        if last in queries_dict:
            result.append(f)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
