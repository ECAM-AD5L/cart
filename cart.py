# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort, request

CART = {
    "cart1":{
            "1":
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
            "2":
                {
                "Id" : "",
                "Nom" : "Macbook Air",
                "Prix" : "2000",
                "Commentaire" : [
                    "Slim and fit !", "Love this product"
                ],
                "Description" : [
                    "red", "Macbook Air 13 pouce"
                ]
               },
            },
    "cart2":{
            "1":{
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
            },
    }

def readAllCarts():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        json string of list of people
    """
    # Create the list of people from our data
    return[CART[key] for key in sorted(CART.keys())]

def readOneCart(nameOfCart):
    """
    This function transmits the token describing the product.
    The data is given to the micro service Item, in return an Id is given to the item.
    :return:        json string with 2 keys : 'Name' and "Description"
    """

    if nameOfCart in CART:
        dictionary = CART.get(nameOfCart)

        # otherwise, nope, not found
    else:
        abort(
            404, "Cart {nameOfCart} not found.".format(nameOfCart=nameOfCart)
        )
    return dictionary

def deleteCart(nameOfCart):
    """
    This function deletes a cart according to the parameter nameOfCart.
    :return:        nothing
    """
    if nameOfCart in CART:
        #TODO : delete dictionary in mongodb.
        print("Cart deleted !")
    else:
        abort(
            404, "Cart '{nameOfCart}' not found.".format(nameOfCart=nameOfCart)
        )
    return "Cart deleted."

def addItem(newItem, nameOfCart):
    """
    This function adds a cart according to the parameter nameOfCart.
    :return:        nothing
    """
    # TODO : add dictionary in mongodb. If new user, create new dictionary (cart 4 for example).
    if nameOfCart in CART:
        print("Item '{id}' suppressed from cart '{nameOfCart}'.".format(id=id, nameOfCart=nameOfCart))
    else:
        abort(
            404, "Cart '{nameOfCart}' not found.".format(nameOfCart=nameOfCart)
        )
    return newItem

def deleteItem(id, nameOfCart):
    """
    This function deletes an item in selected cart.
    :return:        nothing
    """
    # TODO : suppress item in specified cart in mongodb.
    if nameOfCart in CART:
        print("Item '{id}' suppressed from cart '{nameOfCart}'.".format(id=id, nameOfCart=nameOfCart))
    else:
        abort(
            404, "Cart '{nameOfCart}' not found.".format(nameOfCart=nameOfCart)
        )
    return "Cart deleted."




