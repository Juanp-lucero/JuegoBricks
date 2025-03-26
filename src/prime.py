# src/prime.py

def is_prime(n):
    """
    Retorna True si n es un número primo, False en caso contrario.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    num = int(input("Ingrese un número: "))
    if is_prime(num):
        print(f"{num} es un número primo.")
    else:
        print(f"{num} NO es un número primo.")
