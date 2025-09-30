# Fjalekalimi i fiksuar
FJALEKALIMI = "tik12"

# Tentativat e mundshme
tentativa = 3

while tentativa > 0:
    # Merr fjalëkalimin nga përdoruesi
    fjalekalimi = input("Fjalekalimi: ")

    # Kontrollo nëse është i saktë
    if fjalekalimi == FJALEKALIMI:
        print("Hyrje OK")
        break  # Ndalon ciklin nëse fjalëkalimi është i saktë
    else:
        tentativa -= 1  # Ulet numri i tentativave
        print(f"Gabim. Tentativa te mbetura: {tentativa}")

# Njoftim nëse përdoruesi ka humbur të gjitha tentativat
if tentativa == 0:
    print("Ju keni shteruar tentativat.")
