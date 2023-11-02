import logging

# Configura el logger para la clase Calculadora
logger = logging.getLogger('calculadora')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Agrega un controlador de archivo para el registro
file_handler = logging.FileHandler('log.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class Calculadora:
    def __init__(self):
        self.historial = []

    def suma(self, a, b):
        resultado = a + b
        self.historial.append(f"La suma de {a} y {b} es igual a {resultado}")
        return resultado

    def resta(self, a, b):
        resultado = a - b
        self.historial.append(f"La resta de {a} y {b} es igual a {resultado}")
        return resultado

    def multiplicacion(self, a, b):
        resultado = a * b
        self.historial.append(f"La multiplicación de {a} y {b} es igual a {resultado}")
        return resultado

    def division(self, a, b):
        if b == 0:
            raise ValueError("No es posible dividir entre cero.")
        resultado = a / b
        self.historial.append(f"La división de {a} entre {b} es igual a {resultado}")
        return resultado
