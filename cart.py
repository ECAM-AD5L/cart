# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort

# CART = {
#     "cart1":{
#             "item":
#                 {
#                 "Id" : "",
#                 "Nom" : "Macbook Pro",
#                 "Prix" : "2000",
#                 "Commentaire" : [
#                     "Very Good", "Love this product"
#                 ],
#                 "Description" : [
#                     "blue", "Macbook Pro 13 pouce"
#                 ]
#                },
#             },
#     "cart2":{
#             "item":{
#                 "Id" : "",
#                 "Nom" : "Macbook Pro",
#                 "Prix" : "2000",
#                 "Commentaire" : [
#                     "Very Good", "Love this product"
#                 ],
#                 "Description" : [
#                     "blue", "Macbook Pro 13 pouce"
#                 ]
#               },
#             },
#     }
CART = {
    "item":
        {
        "Id" : "",
        "Nom" : "Macbook Pro",
        "Prix" : "2000",
        "Commentaire" : [
            "Very Good", "Love this product"
        ],
        "Description" : [
            "blue", "Macbook Pro 13 pouce"
        ]
       },
    }

def readAllItems():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        json string of list of people
    """
    # Create the list of people from our data
    return[CART[key] for key in sorted(CART.keys())]

def giveToken(nameOfCart):
    """
    This function transmits the token describing the product.
    The data is given to the micro service Item, in return an Id is given to the item.
    :return:        json string with 2 keys : 'Name' and "Description"
    """

    dictionary = CART.get(nameOfCart)
    #
    # return dictionary



