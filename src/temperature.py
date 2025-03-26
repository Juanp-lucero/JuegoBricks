# src/temperature.py

def celsius_to_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convierte grados Fahrenheit a Celsius."""
    return (fahrenheit - 32) * 5/9

if __name__ == "__main__":
    print("Conversor de Temperatura 🌡️")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    opcion = input("Seleccione una opción (1/2): ")

    if opcion == "1":
        celsius = float(input("Ingrese la temperatura en Celsius: "))
        print(f"{celsius}°C = {celsius_to_fahrenheit(celsius):.2f}°F")
    elif opcion == "2":
        fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
        print(f"{fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit):.2f}°C")
    else:
        print("❌ Opción no válida. Intente de nuevo.")
