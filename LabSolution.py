def reverse_pyramid(x):
    '''
    Prints a reverse number pyramid pattern starting from `x` down to 1
    '''
    for i in range(x,0,-1):
        for y in range(i,0,-1):
            print(y, end=" ")
        print()
        
reverse_pyramid(5)

print(reverse_pyramid.__doc__)