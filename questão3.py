import json

# Carregar os dados do JSON
with open('dados.json', 'r') as file:
    faturamento = json.load(file)

# Filtrar valores diferentes de 0
valores_validos = [dado['valor'] for dado in faturamento if dado['valor'] > 0]

# Cálculos
menor_valor = min(valores_validos)
maior_valor = max(valores_validos)
media_mensal = sum(valores_validos) / len(valores_validos)

dias_acima_da_media = sum(1 for dado in faturamento if dado['valor'] > media_mensal)

# Resultados
print(f"Menor valor de faturamento: {menor_valor:.2f}")
print(f"Maior valor de faturamento: {maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")