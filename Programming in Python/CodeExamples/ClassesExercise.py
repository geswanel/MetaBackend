# Creating a base class and checking class and instance object behavior
class House:
    '''
    This is a docstring.
    '''
    num_rooms = 5
    bathrooms = 2

    def cost_evaluation(self):  # self means => instance method
        print("num_rooms =", self.num_rooms)
        pass
        # functionality to evaluate cost

    def check_classmethod():
        print("class method")

def first_exercise():
    h = House() # instantiate
    print(House.num_rooms)  # class attribute
    print(h.num_rooms)  # instance attribute

    h.num_rooms = 7 # changing instance attribute doens't affect class attribute
    print(House.num_rooms)  # class attribute
    print(h.num_rooms)  # instance attribute

    House.num_rooms = 10 # changing class attribute affects all instances attributes if they not changed inside the instance
    print(House.num_rooms)  # class attribute
    print(h.num_rooms)  # instance attribute



# Instantiate
class MyFirstClass:
    print("Who wrote this?")
    index = "Author-Book"

    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)
        print(philosopher + " wrote the book: " + book)

def second_exercise():
    whodunnit = MyFirstClass()
    whodunnit.hand_list("Sun Tzu", "The Art of War")

second_exercise()

