import random

tentativi_rimasti = 5

numero_segreto = random.randint(1, 10)

print("\nIndovina il numero tra 1 e 10!\n")

while tentativi_rimasti > 0:

    print(f"Rimangono {tentativi_rimasti} tentativi.")
    risposta = int(input("Il tuo tentativo: "))

    if risposta < numero_segreto:
        print("Troppo basso!")
    elif risposta > numero_segreto:
        print("Troppo alto!")
    else:
        print("\nRisposta corretta! Hai vinto!")
        break

    tentativi_rimasti -= 1
else:
    print("\nHai perso! Il numero era:", numero_segreto)
