#  Séries Matemáticas - Taylor, Maclaurin e Fourier

Uma aplicação web interativa que demonstra visualmente três importantes séries matemáticas: **Taylor**, **Maclaurin** e **Fourier**.  
Execute **código Python diretamente no navegador** usando **Pyodide**! 🚀

![Matemática Interativa](https://img.shields.io/badge/Matem%C3%A1tica-Interativa-blue)
![Python no Navegador](https://img.shields.io/badge/Python-No%2520Navegador-green)
![HTML5 Web App](https://img.shields.io/badge/HTML5-Web%2520App-orange)

---


---

##  Características

### 🔢 Série de Taylor
**Função:** Aproximação de `ln(x)` em torno de `x = 1`

**Controles:**
- Número de termos: `1–20`
- Intervalo mínimo: `0.1–0.9`
- Intervalo máximo: `1.1–3.0`

**Visualização:**  
Comparação entre a função real e a aproximação polinomial.

---

### 📈 Série de Maclaurin
**Função:** Aproximação de `sin(x)` (série centrada em zero)

**Controles:**
- Número de termos: `1–10`
- Intervalo de visualização: `±5` a `±20`

**Visualização:**  
Evolução da aproximação conforme o número de termos aumenta.

---

### 🌊 Série de Fourier
**Função:** Aproximação de `f(x) = x` no intervalo `[-π, π]`

**Controles:**
- Número de harmônicos: `1–100`

**Visualização:**  
Representação da função **onda quadrada** utilizando senos.

---

##  Tecnologias Utilizadas

| Categoria | Tecnologias |
|------------|--------------|
| **Frontend** | HTML5, CSS3, JavaScript |
| **Execução de Python no Navegador** | [Pyodide](https://pyodide.org/) |
| **Bibliotecas Matemáticas** | NumPy, Matplotlib |
| **Execução Científica** | 100% feita no cliente, sem servidor backend |

---

##  Conceitos Envolvidos

- **Série de Taylor:** aproxima funções suaves por polinômios em torno de um ponto.
- **Série de Maclaurin:** caso especial da série de Taylor centrada em zero.
- **Série de Fourier:** representa funções periódicas como soma de senos e cossenos.

---

##  Como Executar Localmente

1. Clone este repositório:
   em sua pasta de arquivo, abra o CMD e digite git init
   depois git clone https://github.com/ [link do projeto]
