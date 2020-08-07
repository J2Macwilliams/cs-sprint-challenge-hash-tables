#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # create a dict to hold onto tickets
    mydict={}
    
    counter = 0
    # put tickets in dict
    for ticket in tickets:
        mydict[ticket.source] = ticket.destination

    route = []
    # add the start
    # route.append(mydict['NONE'])
    # loop thru dict searching for next value by the keys
    # base case
    for ticket in tickets:
            if ticket.destination is 'NONE':
                    return route
            # check for the start
            if ticket.source is 'NONE':
                route.append(ticket.destination)
            # accumulate destinations and increment counter
            if route[counter] in mydict.keys():
                
                route.append(mydict[route[counter]])
                counter += 1
                # print(route)
    # return route    
    

    

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]
reconstruct_trip(tickets, 3)
        