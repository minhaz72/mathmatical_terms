def fibbonicchi(num:int): 
    if num < 2 : 
        return  1 
    fib_x , fib_nxt  =  1,1 
    i=  3
    while i <=  num: 
        i+=1 
        fib_x  , fib_nxt = fib_nxt , fib_x+  fib_nxt  
        return  fib_nxt 
if __name__=='__main__': 
    for x in range(1, 11 ): 
        print(fibbonicchi(x))
        