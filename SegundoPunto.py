Expresión regular

[A-Za-z][A-Za-z0-9]*

Esta expresión dice que son las comienzan con una letra y pueden continuar con letras o dígitos.

Diseño del AFD

El autómata tiene dos estados:

q0: estado inicial

q1: estado de aceptación

Transiciones:

De q0 a q1 con cualquier letra.

De q1 a q1 con letras o números.

Si aparece cualquier otro símbolo, la cadena es rechazada.

Salida Esperada:

numero ACEPTADO
1X NO ACEPTADO
hola ACEPTADO
x1 ACEPTADO
parcial ACEPTADO
123 NO ACEPTADO
como ACEPTADO
eufareix10 ACEPTADO
1variable NO ACEPTADO
_abc NO ACEPTADO
-- NO ACEPTADO
1a+2b NO ACEPTADO
a3*b3 NO ACEPTADO
a3b3 ACEPTADO
