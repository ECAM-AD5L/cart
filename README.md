# Scalable_architecture
    The purpose of this micro service is to save products in a MongoDB database temporarily.
## Explanations
    - In order to know precisely what the user wants, a SKU has to be determined.
      The last is obtained by requesting it to another micro service.
      For example : Macbook, Pro, i5, 16Go, 256GO SSD, red, ... will give an unique SKU.
    - In order to know if item is in stock, a request with the SKU number is sent to the micro service Stock.
    - If product is in stock a confirmation is sent to the micro service Order.
      When an operation takes place in the card it will notice this to the micro service Order.
    - When the Cart is validated, the content of the last is transferred to the Order micro service.
## Python version
    3.7.1
## Installed packages 
    flask, connexion (pip)