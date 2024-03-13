#le o nome do aluno
#le tres notas
#verifica se são válidas, se não, encerra o programa
#calcula a media final
#imprime o boletim final do aluno

def valida(notas):
    for n in notas:
        if(n>=0) and (n<=10.0): continue #true
        else: #false
            return False 
    #caso toda as notas sejam válidas        
    return True 

def media(notas):
    i= 0
    for n in notas:
        i += n
    return i/3

def boletim(nome, notas):
    if(not valida(notas)): 
        print('!!!notas inválidas!!!\nencerrando...\n')
    else:
        print('\n\n-------Boletim-------')
        print(f'Nome: {nome}\n')
        i = 0
        for n in notas:
            i+=1
            print(f'N{i}: {n}')
        mf = media(notas)
        print('\nMedia Final: %.1lf\n' % mf)
        if (mf < 6): print('Situação Final: REPROVADO')
        else: print('Situação Final: APROVADO')
        

nome = input()
notas = list(map(float,input().split()))

boletim(nome, notas)


#print(nome, n1, n2, n3)


