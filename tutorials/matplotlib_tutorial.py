
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.random.random((2, 2))
y = x * 2

plt.plot(x, y)
plt.title('Values')
plt.xlabel('Valores X')
plt.ylabel('Valores Y')
plt.show()
