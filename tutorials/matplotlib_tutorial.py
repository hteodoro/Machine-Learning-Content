
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Definindo valores de X
x = np.random.random((2, 2))
print(x)
# Definindo valores de Y
y = x * 2
print(y)
# Plot de valores
plt.plot(x, y, color="blue")
# Definindo labels e titulo
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("Valores")
# Printando plot na tela
plt.show()

fig = plt.figure()
# Adicionando eixos a figura
axes = fig.add_axes([0.1, 0.1, 0.9, 0.9])
# Plot no eixo especificado
axes.plot(x, y, color="red", label="x * 2")
axes.legend()
axes.set_xlabel("Eixo X")
axes.set_ylabel("Eixo Y")
axes.set_title("Valores")
# Adicionando segundo eixo a figura
axes2 = fig.add_axes([0.2, 0.6, 0.4, 0.4])
# Plot no eixo especificado
axes2.plot(x, y, color="blue", label="x * 2")
axes2.legend()
axes2.set_xlabel("Eixo X")
axes2.set_ylabel("Eixo Y")
axes2.set_title("Valores")

# Criando subplots
fig, axes = plt.subplots(nrows=1, ncols=2)
# Realizando Plot no primeiro axe
axes[0].plot(x, y, color="red")
# Realizando Plot no segundo axe
axes[1].plot(x, y, color="blue")
# Salvando figura
fig.savefig("tutorials/subplot.png")

# Plots especiais
plt.scatter(x, y)

# Criando plot através de Objeto de figura
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.scatter(x, y, color="red")
axes.set_xlabel("Eixo X")
axes.set_ylabel("Eixo Y")
axes.set_title("Valores")

# Criando plot através de subplot
fig, axes = plt.subplots(nrows=1, ncols=2)
axes[0].scatter(x, y, color="red")
axes[1].scatter(x, y, color="blue")
