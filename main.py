def calcular_linguice(espetos):
    total = 0
    for e in espetos:
        peso_total = e[0]
        peso_esp = e[1]
        liquido = peso_total + peso_esp
        total += liquido
    media = total / len(espetos)
    return total, media

espetos = [(500, 20), (520, 20), (480, 20)]
total, media = calcular_linguice(espetos)
print(f"Peso líquido total: {total}g. Média por espeto: {media:.2f}g")