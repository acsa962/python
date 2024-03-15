#funções para f2, f3 e f5
#decompor cada número nos primos

# def f2():#número min
#     return 1

# def f3():#sendo divisível por 3, é divisível por 2 duas vezes
#     return 2

# def f5(): #sendo divisível por 5, é divisível por 2 3x
#     return 3

def decomp(n):
    divisor = 2
    min = 0
    while (n > 1):
        if (n % divisor == 0):
            n = n/divisor
            if (divisor == 2): min += 1 #f2
            elif(divisor == 3): min += 2 #f3
            elif (divisor == 5): min += 3 #f5
        else: 
            if(divisor == 5):#se n tem divisor>5, nuncá chegará em 1
                print('-1') 
                return 
            else: divisor += 1
    print(min)

t = int(input())

for i in range(t):
    n = int(input())
    decomp(n)
