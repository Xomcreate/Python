# python class and objects
class chisom:
    def __init__(car, brand, year, models, price, maker ):
        car.brand = brand
        car.year = year 
        car.models = models 
        car.price = price
        car.maker = maker


newcar = chisom ("lexus","2022", "SUV", "$1000,0000", "U.S.A")
print(newcar.brand)
print(newcar.price)