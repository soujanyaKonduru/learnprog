# methods no inputs, no outputs
def myfriend():
    print("my friend name is Divya")

myfriend()

# method with one input, no output
def myFriend(name):
    print(f'Hello {name}')

myFriend('Deepti')

# method with no input and one output

def getInformation():
    return "go to google maps to get the directions"

info = getInformation()
print(info)

# method with 2 inputs and one output

def addTwo(x,y):
    z = x + y
    return z

t = addTwo(2,4)
print(t)