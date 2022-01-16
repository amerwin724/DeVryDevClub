#Create a function which draws an equilateral triangle as shown in the picture. This function must accept a parameter
# to indicate size of the output triangle.

def triangle (size):
    space = ' '
    symbol = '*'
    for i in range (size):
        spaces = space*(size-i)
        symbols = symbol*(i+1)
        print(spaces + symbols)
        i += 1

triangle(5)