#se l == r, players = l + r + (ambi//2*2)
#se amb == 0, players = dobro do menor entre l e r

p = list(map(int, input().split())) 
l = p[0]
r = p[1]
amb = p[2]
dif = abs(l-r)#caso sejam diferentes
if (dif>amb): dif = amb

if(l<r): l += dif #l menor
else: r += dif #r menor

#pegando o resto de amb
amb -= dif 

if(amb>0):
    pares = a//2 #pares que ainda podem ser iterados
    l += pares
    r += pares

print(2*min(l, r))

#if(amb == 0):


# if(l == r):
#     print(l+r+(amb//2*2))
# elif(amb==0):
#     if(l>r): 
#         menor = r
#         print(r*2)
#     else: 
#         menor = l
#         print(l*2)
# else: 
#     print(menor*2+(amb//2))

