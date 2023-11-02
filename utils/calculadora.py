class Calculadora:
    def __init__(self): 
        self.historial = []

    def suma(self, a, b):
        try:
            resultado = a + b
            self.historial.append(f"La suma de {a} y {b} es igual a {resultado}")
            return resultado
        except TypeError as e:
            raise ValueError(f"No es posible realizar la suma: {str(e)}")

    def resta(self, a, b):
        try:
            resultado = a - b
            self.historial.append(f"La resta de {a} y {b} es igual a {resultado}")
            return resultado
        except TypeError as e:
            raise ValueError(f"No es posible realizar la resta: {str(e)}")

    def multiplicacion(self, a, b):
        try:
            resultado = a * b
            self.historial.append(f"La multiplicación de {a} y {b} es igual a {resultado}")
            return resultado
        except TypeError as e:
            raise ValueError(f"No es posible realizar la multiplicación: {str(e)}")

    def division(self, a, b):
        try:
            if b == 0:
                raise ValueError("No es posible dividir entre cero.")
            resultado = a / b
            self.historial.append(f"La división de {a} entre {b} es igual a {resultado}")
            return resultado
        except (ZeroDivisionError, ValueError) as e:
            raise ValueError(f"No es posible realizar la división: {str(e)}")
