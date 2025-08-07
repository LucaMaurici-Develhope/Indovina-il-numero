import random

numero_segreto = random.randint(1, 5)

print("\nIndovina il numero tra 1 e 5!\n")

while True:
    risposta = int(input("Il tuo tentativo: "))

    if risposta < numero_segreto:
        print("Troppo basso!")
    elif risposta > numero_segreto:
        print("Troppo alto!")
    else:
        print("\nRisposta corretta!")
        break

print("Fine del gioco, ciao!")