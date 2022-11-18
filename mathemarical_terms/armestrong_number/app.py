n = int(input('enter a number : '))
sum= 0 
temp= n 
while temp >  0 : 
    digit=  temp % 10 
    sum += digit **  3 
    temp //= 10 
if n== sum : 
     print(f'a armestrong number : ')
else: 
    print('not a armestrong number : ')