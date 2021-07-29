def add(*args):
    result = 0
    for num in args:
        result += num
    return result


# print(add(22, 1, 2, 3))


def calculate(n, **kwargs):
    # for key, values in kwargs.items():
    #     pass
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


# calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan", model="Skyline", seats=2)
print(my_car.model)
print(my_car.make)
print(my_car.seats)