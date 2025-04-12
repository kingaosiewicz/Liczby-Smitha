import os
from datetime import datetime

# Tworzenie raportu HTML
now = datetime.now()
fulldate = now.strftime("%d-%m-%Y %H:%M:%S")

outputfile = open("Raport_Smith.html", "w")

outputfile.write(f"""
<html>
  <head>
    <title>Raport Liczby Smitha</title>
  </head>
  <body>
  <h1>Raport Liczby Smitha - {fulldate}</h1>
  <table border="1">
    <tr>
      <th>Input</th>
      <th>Output</th>
    </tr>
    """)

input_dir = "Input"
output_dir = "Output"

# Generowanie raportu na podstawie plików wejściowych i wyjściowych
for i in range(1, 5):
    input_file = os.path.join(input_dir, f"input{i}.txt")
    output_file = os.path.join(output_dir, f"output{i}.txt")

    try:
        with open(input_file, "r") as infile:
            number = int(infile.read().strip())
            with open(output_file, "r") as outfile:
                result = outfile.read().strip()

        # Dodawanie danych do tabeli HTML
        outputfile.write(f"""
        <tr>
          <td>{number}</td>
          <td>{result}</td>
        </tr>
        """)

    except FileNotFoundError:
        outputfile.write(f"""
        <tr>
          <td>{f"input{i}.txt"}</td>
          <td>Plik nie istnieje.</td>
        </tr>
        """)
    except ValueError:
        outputfile.write(f"""
        <tr>
          <td>{f"input{i}.txt"}</td>
          <td>Niepoprawny format liczby.</td>
        </tr>
        """)

outputfile.write("""
  </table>
  </body>
</html>
""")

outputfile.close()

print("Raport HTML został wygenerowany.")
