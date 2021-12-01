import time

#1)transforma o tempo do formato 00:00:00 em segundos
def seconds(time):
  h, m, s = time.split(':')
  soma = int(h) * 3600 + int(m) * 60 + int(s)
  return soma
  
print(str(seconds('00:27:15')) + " segundos")

#2)cáculo da velocidade em m/s
def velocidadeM(input):
    vel = input / seconds('00:27:15')
    return vel

print(str(velocidadeM(5000)) + " m/s")

#3)transforma a velocidade de m/s em km/h
def velocidadeKm(input):
    vel2 = (input/1000)/(seconds('00:27:15')/3600) #aqui chama a função seconds(time), coloquei um exemplo para rodar e ver se estava funcionando
    return vel2

print(str(velocidadeKm(5000)) + " Km/h")

#4)calcula o tempo em segundos de prova conforme o objetivo do atleta 
def tempoProva(objective, test): #objetivo e o teste realizado em metros
  a = (objective/test)**1.06
  tempoTeste = seconds('00:27:15')
  tempoProvaS =  a * tempoTeste #tempo estimado da prova em segundos
  return tempoProvaS

print(str(tempoProva(10000, 5000)) + " segundos estimados para realizar uma prova de 10000 m")

#5)converte o tempo de prova para o formato 00:00:00
def tempoProvaM(tempoProva):
  return time.strftime("%H:%M:%S", time.gmtime(tempoProva(10000, 5000))) #convertendo segundos para o formato 00:00:00

print("Tempo necessário para realizar uma prova de 10000 m: " + str(tempoProvaM(tempoProva)))

#6)calcula a velocidade mmédia da prova em km/h
def velocidadeMedia(objective, tempoProva):
  return (objective/1000)/(tempoProva(10000, 5000)/3600)

print("Velocidade média em km/h é: " + str(velocidadeMedia(10000, tempoProva)))

