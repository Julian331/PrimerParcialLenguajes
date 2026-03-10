# Punto 1 – AFD para movimientos de ajedrez

Se definió una expresión regular para representar movimientos
de ajedrez como:

p->k4
qXpe5

donde:

p,k,q,b,n,r representan las piezas del ajedrez.

-> representa un movimiento.
X representa una captura.

La posición del tablero se representa mediante una columna
(a-h) y una fila (1-8).

Expresión regular:

(p|k|q|b|n|r)(->|X)(p|k|q|b|n|r)([a-h]?[1-8])

El programa lee los movimientos desde el archivo pruebas.txt
y muestra si cada cadena es aceptada o rechazada por el AFD.

Salida Esperada:
p->k4 
qXpe5 
r->na3 
p-k4 
z->k4 
kXra8 
b->qd2 
buentrabajo 
123 
