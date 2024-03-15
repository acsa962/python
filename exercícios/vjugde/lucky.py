n = list(input())

qtd = 0

for i in n:
    if(i == '4') or (i == '7'): qtd+=1

if (qtd == 4) or (qtd == 7): print('YES')
else: print('NO')