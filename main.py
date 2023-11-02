import logging
from utils.calculadora import Calculadora

# Configura el logger para el programa principal
logger = logging.getLogger('calculadora_main')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Agrega un controlador de archivo para el registro
file_handler = logging.FileHandler('log.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def main():
    calculadora = Calculadora()
    operaciones = {
        '+': calculadora.suma,
        '-': calculadora.resta,
        '*': calculadora.multiplicacion,
        '/': calculadora.division
    }

    while True:
        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
        except ValueError:
            logger.error("Entrada inválida: Se esperaban números.")
            print("Por favor, ingrese números válidos.")
            continue

        operacion = input("Elija una operación (+, -, *, /): ")

        if operacion in operaciones:
            if operacion == '/' and b == 0:
                print("Error: No es posible dividir entre cero.")
                continue
            try:
                resultado = operaciones[operacion](a, b)
            except Exception as e:
                logger.error(f"Error en la operación: {str(e)}")
                continue
        else:
            logger.error("Operación no válida.")
            print("Operación no válida")
            continue

        print(f"Resultado: {resultado}")

        salir = input("¿Desea salir? (si/no): ").lower()
        if salir == "si":
            break

    for operacion in calculadora.historial:
        print(operacion)

if __name__ == "__main__":
    main()
