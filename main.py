import os

def sum_of_digits(n):
    """Funkcja do obliczania sumy cyfr liczby."""
    return sum(int(digit) for digit in str(n))

def is_prime(n):
    """Funkcja do sprawdzania, czy liczba jest pierwsza."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    """Funkcja do znajdowania dzielników pierwszych liczby."""
    factors = []
    for i in range(2, n + 1):
        while n % i == 0 and is_prime(i):
            factors.append(i)
            n //= i
    return factors

def is_smith_number(n):
    """Funkcja do sprawdzania, czy liczba jest liczbą Smitha."""
    if is_prime(n):
        return False  # Liczba musi być złożona

    # Suma cyfr liczby n
    sum_n = sum_of_digits(n)

    # Dzielniki pierwsze
    factors = prime_factors(n)

    # Suma cyfr dzielników pierwszych
    sum_factors = sum(sum_of_digits(factor) for factor in factors)

    return sum_n == sum_factors

# Główna część programu
input_dir = "Input"
output_dir = "Output"
os.makedirs(output_dir, exist_ok=True)

for i in range(1, 5):
    input_file = os.path.join(input_dir, f"input{i}.txt")
    output_file = os.path.join(output_dir, f"output{i}.txt")

    try:
        with open(input_file, "r") as infile:
            number = int(infile.read().strip())
            result = (f"Liczba {number} jest liczba Smitha." if is_smith_number(number)
                      else f"Liczba {number} nie jest liczba Smitha.")

        with open(output_file, "w") as outfile:
            outfile.write(result)

    except FileNotFoundError:
        print(f"Plik input{i}.txt nie istnieje.")
    except ValueError:
        print(f"Plik input{i}.txt nie zawiera poprawnej liczby.")