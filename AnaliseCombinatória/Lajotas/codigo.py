n = 1
while(n != 0):
    a = 2
    b = 1
    aux = 0
    n = int(input())
        
    if(n == 1):
        print(1)
        
    elif(n == 2):
        print(2)
        
    elif(n >= 3 and n <= 40):
        for i in range (0, (n - 2)):
            aux = a
            a = a + b   
            b = aux
        print(a)
    
