numero_segreto = 4

print("\nIndovina il numero tra 1 e 10!\n")

risposta = input("Il tuo tentativo: ")

risposta = int(risposta)

if numero_segreto == risposta:
    print("\nRisposta corretta!")
else:
    print("\nRisposta sbagliata!")

