import matplotlib.pyplot as plt
from scipy import stats

x = [315, 960, 1635]
y = [1000, 3000, 5000]

#parâmetros importantes da regressão linear (y = a * x +b): slope= a; intercept =b; r= o R ao quadrado da reta; std_err = erro padrão
slope, intercept, r, p, std_err = stats.linregress(x, y)

#função pra descobrir o valor y(tempo) dando o valor de x (distância)
def myfunc(x):
  return slope * x + intercept

#roda cada valor de x dentro da função e gerar um novo array com novos valores de y
mymodel = list(map(myfunc, x))
print("Slope: " + str(slope))
print("intercept: " + str(intercept))
print("r: " + str(r))
print("p: " + str(p))
print("std_err: " + str(std_err))

plt.scatter(x, y) #plota os pontos
plt.plot(x, mymodel) #desenha a linha
plt.show() #mostra o gráfico