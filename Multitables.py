# define how mytable do here.
def mytable(table): 
    for i in range(1,11,1):
        result = table * i
        print(f'{table} *  {i} = {result}')

# Use the my table with 3
mytable(3)

# Use the my table with 4
mytable(4)

# Use the my table with 5
mytable(5)


for i in range(1,11,1):
    mytable(i)
    