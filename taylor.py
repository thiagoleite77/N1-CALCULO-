import numpy as np
import matplotlib.pyplot as plt

def taylor_ln(x, n):
    """Aproxima ln(x) em torno de x = 1 com n termos."""
    terms = [((-1)**(k+1)) * ((x-1)**k) / k for k in range(1, n+1)]
    return np.sum(terms)

# Amostragem
x_vals = np.linspace(0.5, 2, 200)
real_ln = np.log(x_vals)

plt.figure()
plt.plot(x_vals, real_ln, label='ln(x) real')

# Mostrar aproximações
for n in [1, 2, 4, 8]:
    approx = [taylor_ln(x, n) for x in x_vals]
    plt.plot(x_vals, approx, label=f'{n} termos')

plt.title("Aproximação de ln(x) com Série de Taylor (centro = 1)")
plt.grid()
plt.legend()
plt.show()
