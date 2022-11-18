def armestrong(num:int): 
    sum= 0 
    tem=  num 
    while tem > 0 : 
        digit= tem %  10 
        sum += digit**3 
        tem//=10 
    if num== sum : 
        print('num is a armestrong number ')
    else:
        print('num is not a armestrong number : ')