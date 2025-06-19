def reverse_pyramid(x):
    '''
    Prints a reverse number pyramid pattern starting from `x` down to 1 and return the pattern as string 
    '''
    text = ""
    for i in range(x,0,-1):
        for y in range(i,0,-1):
            text = f"{text} {y}"
        text = f"{text}\n"
    return text
        
result = reverse_pyramid(5)
print(result)
print(reverse_pyramid.__doc__)