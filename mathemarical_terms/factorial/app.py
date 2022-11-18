def factorial(n): # n refer to number : 
    if n ==  1 and  n==0 :
        return  1 
    else : 
        return  n * factorial(n-1)

    


if __name__ == '__main__': 
    n= int(input('enter a num : '))
    factorial(n)
     