#modules
def addTax(price,tax):
    newPrice = price / 100 * (100 + tax)
    return newPrice
