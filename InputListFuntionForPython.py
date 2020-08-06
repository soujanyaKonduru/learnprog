
# input
name = input('please enter your name:')
# print with formatting
# you can use 'f' (formatting) with print like below
name = "sai"
print(f'Hello {name} welcome')

# with f in print function the variables in { and } will be replaced with its values

# list
# list is used to hold a variable with multiple values.
hobbies = ['play', 'music', 'running']

# for
# we can use for loop to do repetive tasks and also looping over the lists 
for hobby in hobbies:
    print(f'my hobby is {hobby}')

# also for looping over given numbers we can use range function like below

for x in range(1,10,1):
    print(x)

# range function will have start, end and increment. In above start=1, end=10 and increment=1