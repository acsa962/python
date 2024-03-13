#verifica se o número é par ou impar

def modulo(num):
    resto = num - ((num//2)*2)
    #print(f'resto ==> {resto}')
    if(resto==0): print('par')
    else: print('impar')

def verifica(num):
    if(num%2 != 0): print('impar')
    else: print('par')

num = int(input())
#modulo(num)
verifica(num)


