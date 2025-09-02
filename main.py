import random
print ("seleziona difficoltà") 
print("1: Facile: numero di tentativi= 5")
print("2: Difficile: numero di tentativi= 2")
risposta= input ("seleziona difficoltà")
if risposta== "1": 
    print("hai selezionato facile")
    tentativi_rimasti=5
elif risposta== "2": 
    print("hai selezionato difficile")
    tentativi_rimasti=2
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