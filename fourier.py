import numpy as np
import matplotlib.pyplot as plt

def fourier_series(x, n_terms):
    """Aproxima f(x)=x pela Série de Fourier com n_terms harmônicos."""
    result = np.zeros_like(x)
    for n in range(1, n_terms+1):
        result += 2*((-1)**(n+1) / n) * np.sin(n*x)
    return result

# Amostragem
x_vals = np.linspace(-np.pi, np.pi, 600)
plt.figure()
plt.plot(x_vals, x_vals, label='f(x)=x real')

# Mostrar aproximações
for n in [1, 3, 10, 50]:
    plt.plot(x_vals, fourier_series(x_vals, n), label=f'{n} harmônicos')

plt.title("Série de Fourier — f(x)=x")
plt.grid()
plt.legend()
plt.show()
