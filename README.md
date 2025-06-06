# Smith Number Checker

Aplikacja w języku Python służąca do sprawdzania, czy dana liczba jest liczbą Smitha. Program przetwarza dane z plików wejściowych, zapisuje wyniki do plików wyjściowych, generuje raport HTML oraz udostępnia prosty interfejs w postaci menu.

---

## Czym jest liczba Smitha?

**Liczba Smitha** to liczba złożona, dla której suma cyfr jest równa sumie cyfr jej czynników pierwszych.  
**Przykład:**  
Liczba 202 → 2 + 0 + 2 = 4  
Rozkład na czynniki pierwsze: 2 × 101 → 2 + 1 + 0 + 1 = 4  
Zatem 202 jest liczbą Smitha.

---

## Struktura projektu

- `main.py` – główny program: sprawdza liczby z folderu `Input/` i zapisuje wyniki do `Output/`.
- `raport.py` – generuje raport HTML (`Raport_Smith.html`) zawierający dane wejściowe i odpowiadające im wyniki.
- `menu.bat` – menu w wierszu poleceń z opcjami:
  - START – uruchamia przetwarzanie danych i raport
  - INFORMACJE – wyjaśnienie działania programu
  - BACKUP – tworzy kopię zapasową danych
  - ZAKOŃCZ – kończy działanie programu

---

## Uruchomienie

1. Utwórz foldery `Input/` i `Output/`.
2. W folderze `Input/` umieść pliki `input1.txt`, `input2.txt` itd. – każdy z liczbą całkowitą w środku.
3. Uruchom plik `menu.bat`.
4. Wybierz opcję **1 (START)**, aby:
   - Sprawdzić liczby z plików
   - Zaktualizować pliki wyjściowe w `Output/`
   - Wygenerować raport `Raport_Smith.html`

---

## Kopia zapasowa

Opcja **BACKUP** tworzy folder z aktualną datą i godziną, a w nim zapisuje:
- katalogi `Input/` i `Output/`
- plik `Raport_Smith.html`

---
Feel free to explore the code <3
