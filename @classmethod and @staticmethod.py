class PlayerCharacter:
    #Class Object Attribute
    membership = True
    def __init__(self, name='anonymous', age=21):
        self.name = name #attributes
        self.age = age

    def shout(self):
        print(f'my name is {self.name}')


    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num 2

player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)
player3 = PlayerCharacter.adding_things(7,7)

print(player2.name)

print(player3.age)
