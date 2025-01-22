#!/bin/bash

# Controlla se è stato passato un argomento (il valore di x)
if [ "$#" -ne 1 ]; then
    echo "Uso: $0 <x>"
    exit 1
fi

# Assegna l'argomento a una variabile
x=$1

# Controlla se esiste la cartella input, output e my_output
if [ ! -d "input" ]; then
    echo "Errore: La cartella 'input' non esiste"
    exit 1
fi

if [ ! -d "output" ]; then
    echo "Errore: La cartella 'output' non esiste"
    exit 1
fi

if [ ! -d "my_output" ]; then
    mkdir -p my_output
fi

# Inizializza un contatore per l'output
counter=1

# Itera su tutti i file nella cartella input
for file in input/input*.txt; do

    input_file="input/input${counter}.txt"
    echo "$input_file"
    # Controlla che il file esista (gestione di casi in cui input*.txt non corrisponde a nulla)
    if [ ! -e "$input_file" ]; then
        echo "Nessun file trovato nella cartella 'input'"
        exit 1
    fi

    # Costruisce il nome del file di output e del file di output originale
    output_file="my_output/out${counter}.txt"
    orig_output_file="output/output${counter}.txt"

    # Lancia il comando richiesto
    python3 "$x" < "$input_file" > "$output_file"

    # Controlla le differenze con il file nella cartella 'output'
    output=$(diff "$output_file" "$orig_output_file") # Esegui il comando e cattura l'output

    if [[ -n "$output" ]]; then
        echo "File: $input_file"
        echo "$output"
        echo "File: $output_file"
        echo "File: $orig_output_file"
    fi

    # Incrementa il contatore
    counter=$((counter + 1))
    
done

echo "Operazione completata"
