palabra = input("Escribe una palabra: ")

arbalap = palabra[::-1]

print(arbalap)

if arbalap == palabra:
    print(f"Como {palabra} = {arbalap}, entonces\n{palabra} es un palíndromo")
else:
    print(f"Como {palabra} es distinto de {arbalap} entonces\n {palabra} NO es un palíndromo")