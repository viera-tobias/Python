# calculadora.py
import math

class Calculadora:
    def suma(self, a, b):
        """Suma dos números"""
        return a + b # retorna la suma: by Moises

    def resta(self, a, b):
        """Resta dos números"""
        return a - b #retorna la resta: by Tobias

    def multiplicacion(self, a, b):
        """Multiplica dos números"""
        return a * b #retorna la multiplicacion: by Tobias
        

    def division(self, a, b):
        """Divide dos números"""
        return  a / b #retorna la division: by Tobias

    def potencia(self, base, exponente):
        """Calcula la potencia de un número"""
        return (f"la potencia es"+ base ** exponente)

    def raiz_cuadrada(self, a):
        """Calcula la raíz cuadrada de un número"""
        pass

    def modulo(self, a, b):
        """Calcula el módulo (resto) de la división"""
        pass

    def logaritmo(self, a, base=10):
        """Calcula el logaritmo de un número con base 10 por defecto"""
        if a <= 0:
            raise ValueError("El argumento 'a' debe ser mayor que 0")

        return math.log10(a)

    def valor_absoluto(self, a):
        """Devuelve el valor absoluto de un número"""
        pass

    def maximo(self, a, b):
        """Devuelve el número mayor entre dos"""
        pass


def main():
    calc = Calculadora()
    print("Calculadora lista para implementar funciones.")


if __name__ == "__main__":
    main()
