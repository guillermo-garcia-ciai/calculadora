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

            if not a.is_integer() or not b.is_integer():
                raise ValueError("Los números deben ser enteros.")
        except ValueError as e:
            logger.error(f"Entrada inválida: {str(e)}")
            print(f"Por favor, ingrese dos números enteros.")
            continue

        operacion = input("Elija una operación (+, -, *, /): ")

        if operacion in operaciones:
            if operacion == '/' and b == 0:
                print("Error: No es posible dividir entre cero.")
            else:
                try:
                    resultado = operaciones[operacion](a, b)
                    print(f"Resultado: {resultado}")
                except ValueError as e:
                    logger.error(f"Error en la operación: {str(e)}")
        else:
            logger.error("Operación no válida.")
            print("Operación no válida")
            continue

        salir = input("¿Desea salir? (si/no): ").lower()
        if 'si' in salir:
            break

    for operacion in calculadora.historial:
        print(operacion)

if __name__ == "__main__":
    main()
