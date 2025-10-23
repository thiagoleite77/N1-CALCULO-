import numpy as np
import matplotlib.pyplot as plt
import math

def maclaurin_sin(x, n):
    """Aproxima sin(x) com n termos da Série de Maclaurin."""
    result = sum(((-1)**k) * (x**(2*k+1)) / math.factorial(2*k+1) for k in range(n))
    return result

# Amostragem
x_vals = np.linspace(-10, 10, 400)
plt.figure()
plt.plot(x_vals, np.sin(x_vals), label='sin(x) real')

# Mostrar aproximações
for n in [1, 2, 4, 6]:
    approx = [maclaurin_sin(x, n) for x in x_vals]
    plt.plot(x_vals, approx, label=f'{2*n+1} termos')

plt.title("Aproximação de sin(x) — Série de Maclaurin")
plt.grid()
plt.legend()
plt.show()
