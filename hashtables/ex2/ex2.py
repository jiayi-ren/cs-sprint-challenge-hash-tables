#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    trip = {}
    for ticket in tickets:
        trip[ticket.source] = ticket.destination

    route = []
    next = trip["NONE"]
    while next != "NONE":
        route.append(next)
        next = trip[next]
    route.append("NONE")

    return route
