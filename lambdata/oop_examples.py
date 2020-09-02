import pandas as pd

#pd.DataFrame is the DataFrame class
# You can make children of classes you didn't write!
# As an exercise try to use and/or build on this!
class MyDataFrame(pd.DataFrame):
    def num_cells(self):
        return self.shape[0] * self.shape[1]


class BareMinimumClass:
    pass


class Complex:
    def __init__(self, realpart, imagpart):
        """
        Constructor for Complex Numbers.
        Complex numbers are part real, part imaginary
        Imaginary numbers are roots of negative numbers
        """
        self.r = realpart
        self.i = imagpart

    def add(self, other_complex):
        self.r += other_complex.r
        self.i += other_complex.i

    def __repr__(self):
        return '({}, {})'.format(self.r, self.i)

class SocialMediaUser:
    def __init__(self, name, location, upvotes=0):
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)

    def recieve_upvote(self):
        self.upvotes += 1
    
    def is_popular(self):
        return self.upvotes >100

class Animal:
    """General representation fof animals."""
    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        self.weight = float(weight)
        self.diet_type = diet_type

    def run(self):
        return 'Vroom!'

    def eat(self, food):
        return food + 'is delicious, yum!'

class Tiger(Animal):
    def __init__(self, name, weight, diet_type, num_stripes):
        super().__init__(name, weight, diet_type)
        self.num_stripes = int(num_stripes)

    def say_great(self):
        #method that only exists for tigers
        return "it's GREEEAAAAT!"

    def run(self):
        # overriding run to be different for tigers
        return 'Scamperwooshhh!'



if __name__ == '__main__':
    #demo code if you run 'python oop_examples.py'
    #example0
    b = BareMinimumClass()
    #example 1
    num1 = Complex(3, -5)
    num2 = Complex(-1, 6)
    num1.add(num2)
    print(num1.r, num1.i)
    #example 2
    user1 = SocialMediaUser('Tim', 'Philadelphia')
    user2 = SocialMediaUser('Omar', 'Los Angelas', upvotes=50)
    user3 = SocialMediaUser('Erle', 'Florida')
    print(user2.is_popular())
    for _ in range(75):
        user2.recieve_upvote()
    print(user2.is_popular())