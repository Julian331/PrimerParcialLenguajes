# Punto 3 – Método de Newton para aproximar raíces
---
## Método de Newton

El método se basa en la siguiente fórmula iterativa:

[
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
]

donde:

* (x_n) es la aproximación actual
* (f(x)) es la función
* (f'(x)) es la derivada de la función

En cada iteración se obtiene una **mejor aproximación de la raíz**.

---

## Implementación

El programa fue diseñado para calcular la raíz de la función:

[
f(x) = x^2 - 2
]

La raíz de esta función corresponde a:

[
\sqrt{2}
]

El algoritmo comienza con un valor inicial y realiza varias iteraciones para mejorar la aproximación.

---

## Ejecución del programa

Al ejecutar el programa se obtiene una serie de aproximaciones:

```id="6z2p9g"
Iteracion 0 -> x = 1.500000
Iteracion 1 -> x = 1.416667
Iteracion 2 .....
```




RESULTADO:

<img width="502" height="243" alt="image" src="https://github.com/user-attachments/assets/d9e6e5f2-150b-4826-ad55-0181d259cfe1" />
