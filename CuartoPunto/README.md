



TIEMPO EN HASKELL:


<img width="654" height="121" alt="image" src="https://github.com/user-attachments/assets/2df01dfb-e2f5-45c8-a3bb-107f1a8b6df7" />


TIEMPO EN C:


<img width="684" height="85" alt="image" src="https://github.com/user-attachments/assets/870f287c-6936-43c9-ba87-f843897278c2" />


PRUEBAS DE VARIOS NUMEROS EN C:


<img width="785" height="217" alt="image" src="https://github.com/user-attachments/assets/9f56e199-7190-4b5f-95a4-6f7c656be998" />

---

# Algoritmo de Euclides

El algoritmo de Euclides calcula el MCD de dos números utilizando la siguiente definición recursiva:

```text
MCD(a,b) = a        si b = 0
MCD(a,b) = MCD(b,a mod b)  si b ≠ 0
```

Este algoritmo es muy eficiente debido a que reduce rápidamente el tamaño de los números mediante la operación módulo.

---

# Implementación en C (Paradigma Imperativo)

En C el algoritmo se implementa utilizando **recursión y control explícito del flujo del programa**.

Características:

* manejo directo de variables
* control explícito de la memoria
* ejecución muy cercana al hardware

Para medir el rendimiento, el algoritmo se ejecutó **1,000,000 de veces** utilizando la función `clock()`.

Resultado obtenido:

```text
MCD = 9
Tiempo C: 0.031089 segundos
```

---

# Implementación en Haskell (Paradigma Funcional)

En Haskell el algoritmo se expresa de manera **más cercana a su definición matemática** mediante funciones recursivas.

Características:

* uso de funciones puras
* ausencia de estado mutable
* estilo declarativo

También se ejecutó el algoritmo **1,000,000 de veces** para medir el tiempo de ejecución.

Resultado aproximado:

```text
9
0.04s
```

---

# Comparación de Paradigmas

| Característica       | C                   | Haskell               |
| -------------------- | ------------------- | --------------------- |
| Paradigma            | Imperativo          | Funcional             |
| Estilo               | Control paso a paso | Definición matemática |
| Manejo de estado     | Variables mutables  | Inmutabilidad         |
| Nivel de abstracción | Bajo                | Alto                  |

---

# Comparación de Rendimiento

| Lenguaje | Tiempo aproximado |
| -------- | ----------------- |
| C        | 0.031 s           |
| Haskell  | ~0.04 s           |

Observaciones:

* **C es ligeramente más rápido**, debido a su compilación directa a código máquina.
* **Haskell introduce cierta sobrecarga** debido a su modelo de ejecución funcional y runtime.
* La diferencia es pequeña porque el algoritmo de Euclides es extremadamente eficiente.

---

# Conclusión

El algoritmo de Euclides puede implementarse eficientemente en ambos paradigmas. Sin embargo, cada lenguaje refleja una filosofía de programación distinta:

* **C** prioriza el control y la eficiencia.
* **Haskell** prioriza la claridad matemática y la expresividad.

A pesar de las diferencias de paradigma, ambos lenguajes producen resultados correctos y tiempos de ejecución muy bajos para este algoritmo.

---
