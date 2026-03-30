import csv
import os

# Percorso dei file
input_file = os.path.join('data', 'file_input.csv')
output_file = os.path.join('data', 'file_output.csv')

# Leggere i dati dal file CSV di input
with open(input_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    data = list(reader)

# Ordinare i dati per stipendio decrescente
data.sort(key=lambda x: int(x['stipendio']), reverse=True)

# Scrivere i dati ordinati nel file CSV di output
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    if data:
        writer = csv.DictWriter(f, fieldnames=data[0].keys(), delimiter=';')
        writer.writeheader()
        writer.writerows(data)

print("File CSV ordinato creato con successo in", output_file)
