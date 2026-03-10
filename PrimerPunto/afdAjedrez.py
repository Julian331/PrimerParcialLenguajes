class AFD_Ajedrez:

    def __init__(self):
        self.piezas = {'p','k','q','b','n','r'}
        self.columnas = {'a','b','c','d','e','f','g','h'}
        self.filas = {'1','2','3','4','5','6','7','8'}

    def validar(self, cadena):

        i = 0
        n = len(cadena)

        # pieza inicial
        if i < n and cadena[i] in self.piezas:
            i += 1
        else:
            return False

        # operador
        if i < n and cadena[i] == '-':
            i += 1
            if i < n and cadena[i] == '>':
                i += 1
            else:
                return False
        elif i < n and cadena[i] == 'X':
            i += 1
        else:
            return False

        # segunda pieza
        if i < n and cadena[i] in self.piezas:
            i += 1
        else:
            return False

        # puede venir columna o fila directamente
        if i < n and cadena[i] in self.columnas:
            i += 1

        # fila obligatoria
        if i < n and cadena[i] in self.filas:
            i += 1
        else:
            return False

        return i == n


afd = AFD_Ajedrez()

with open("pruebas.txt") as f:
    for linea in f:
        cadena = linea.strip()

        if afd.validar(cadena):
            print(cadena, "ACEPTADO")
        else:
            print(cadena, "RECHAZADO")
