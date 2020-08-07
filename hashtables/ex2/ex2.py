#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # create a dict to hold onto tickets
    mydict={}
    
    counter = 0
    # put tickets in dict
    for ticket in tickets:
        mydict[ticket.source] = ticket.destination

    route = []
    count = 0
     # add the start
    place = mydict['NONE']
    route.append(place)
    while len(route) < length:
        # accumulate destinations
        next = mydict[route[count]]
        route.append(next)
        count += 1
    return route 
    
        