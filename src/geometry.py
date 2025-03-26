# src/geometry.py

import math

def area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    return math.pi * radio ** 2

def area_rectangulo(base, altura):
    """Calcula el área de un rectángulo."""
    return base * altura

def area_triangulo(base, altura):
    """Calcula el área de un triángulo."""
    return (base * altura) / 2

if __name__ == "__main__":
    print("Calculadora de Áreas 📏")
    print("1. Círculo")
    print("2. Rectángulo")
    print("3. Triángulo")
    
    opcion = input("Seleccione una opción (1/2/3): ")

    if opcion == "1":
        radio = float(input("Ingrese el radio del círculo: "))
        print(f"Área del círculo: {area_circulo(radio):.2f} unidades cuadradas.")
    
    elif opcion == "2":
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        print(f"Área del rectángulo: {area_rectangulo(base, altura):.2f} unidades cuadradas.")
    
    elif opcion == "3":
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        print(f"Área del triángulo: {area_triangulo(base, altura):.2f} unidades cuadradas.")
    
    else:
        print("❌ Opción no válida. Intente de nuevo.")
