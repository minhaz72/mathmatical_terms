def factor(num:int): 
    print(f'the factor of {num}  is: ')
    for i in range(1, num+1) : 
        if num %  i == 0 : 
            print(f' the facotor are {i} ')
num=  input('enter a num : ')
factor(num )
  