pesetas = float(input("¿Cuantas pesetas tienes?: "))
valor_euro = 166.386
euros = round(pesetas / valor_euro, 2)

euros = str(euros)
print(f"Tienes {euros} €uros")