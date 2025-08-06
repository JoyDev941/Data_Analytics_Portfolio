#a decorator extends the functionality of a function, without changing the base of what is already does.

def add_wheel(funct):
    def wrapper():
        print("*Added Wheels*")
        funct()
    return wrapper

def add_paint(funct):
    def wrapper():
        print("*Added Paint*")
        funct()
    return wrapper

@add_wheel
@add_paint
def create_car():
    print("Car shell added")


create_car()

#to keep the idea simple, its simply a modular way too add additional functionality to a base function. 
#check the additional ipynb file for more examples