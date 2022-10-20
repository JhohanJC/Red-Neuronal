#Red Neuronal Simple (Una Neurona)
X=[1,1] #Entradas
W=[0.8,0.9] #Pesos
b=0.5 #bias
h = sum([(W[k2]*X[k2])  for k2 in range(len(X))])+b # h=W*X+b
def sigmoid(x): return 1/(1+2.7183**(-x)) # Función de activación
neuron=sigmoid(h) # Salida de la neurona
print(neuron)
