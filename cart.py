def readAllItems():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        json string of list of people
    """
    # Create the list of people from our data
    return [CART[key] for key in sorted(PEOPLE.keys())]
