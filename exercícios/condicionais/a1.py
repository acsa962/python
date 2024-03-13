#leia um número real
#se for positivo, imprima a raíz
#se não, imprima o número ao quadrado

import math

def func(num):
    if(num>0): #positivo
        print(math.sqrt(num))
    else: #negativo
        print(num*num) 


num = float(input())
func(num)