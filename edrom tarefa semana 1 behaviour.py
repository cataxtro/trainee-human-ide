import sys

print("A coordenada x do retangulo vai de -1000 a 1000.")
print("A coordenada y do retangulo vai de -1000 a 1000.")
print("Entre com as coordedanas x e y do ponto escolhido.")

x = input("Coordenada x eh: ")
y = input("Coordenada y eh: ")

coordenada = (int(x), int(y))
print(coordenada)

if (int(x) > 1000 or int(x) < -1000 or int(y) > 1000 or int(y) < -1000):{
  print("Ponto escolhido fora da malha.")
 }
else:

 if(int(x) > 0 and int(y) > 0):
  print("o ponto escolhido esta a direita e para cima em relacao a origem en (0,0).")
 elif (int(x) > 0 and int(y) < 0):
  print("o ponto escolhido esta a direta e para baixo em relacao a origem en (0,0).")
 if (int(x) < 0 and int(y) > 0):
  print("o ponto escolhido esta a esquerda e para cima em relacao a origem em (0,0).")
 elif (int(x) < 0 and int(y) > 0):
  print("o ponto escolhido esta a esquerda e para baixo em relacao a origem em (0,0).")
 if (int(x) > 0 and int(y) == 0):
  print("o ponto esta para a direita en relacao a origen en (0,0)")
 elif (int(x) < 0 and int(y) == 0):
  print("o ponto esta para a esquerda en relacao a origen en (0,0)")