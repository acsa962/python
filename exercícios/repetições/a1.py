# decomposição em primos

def decomp(num):
    divisor = 2
    while (num > 1):
        if (num % divisor == 0):
            print(num, divisor)
            num = num/divisor
        else: divisor += 1

num = int(input())

decomp(num)


