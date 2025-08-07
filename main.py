import random

numero_segreto = random.randint(1, 5)

print("\nIndovina il numero tra 1 e 5!\n")

da_indovinare = True

while da_indovinare == True:
    risposta = int(input("Il tuo tentativo: "))

    if numero_segreto == risposta:
        print("\nRisposta corretta!")
        da_indovinare = False
    else:
        print("\nRisposta sbagliata!")
else:
    print("Fine del gioco, ciao!")



