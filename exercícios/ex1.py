# o automóvel faz 12km/h
# tempo * velocidade / 12

tempo = input()
velocidade = input()

distancia = float((int(velocidade) * int(tempo))/12)

print('%.3lf' % distancia)