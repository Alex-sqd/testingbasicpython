texto = input("Escribe una palabra:\n")

capitalize_texto = texto.capitalize()
upper_texto = texto.upper()
lower_texto = texto.lower()
strip_texto = texto.strip()
replace_in_text = texto.replace('o', 'a')

print(capitalize_texto)
print(upper_texto)
print(lower_texto)
print(strip_texto)
print(replace_in_text)

print(len(texto))
print(texto.count('a'))

length = len(texto)

for i in range(0, length):
    print(texto[i])