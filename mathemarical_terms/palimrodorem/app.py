def palindrome( num: int ) : 
    reverse= num[::-1]
    if num ==  reverse : 
        print(f'this{num}  is palindrome ')
    else: 
        print('not palindrome')
        