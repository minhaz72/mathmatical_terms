def Floyds_triangle(row:int): 
    n= 0 
    for i in range(row) : 
        for j in range(i+1) : 
            print(n,  end='')
            n+=1 
        print()
if __name__ ==  '__main__' : 
    row=input('enter the number of row you  want L ')
    Floyds_triangle(row)
    