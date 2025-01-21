def inverter_string(s):
    """
    Inverte os caracteres de uma string sem usar funções prontas como reverse.
    """
    invertida = ""
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

# Entrada da string (pode ser definida aqui ou pelo usuário)
string_original = input("Informe a string a ser invertida: ")  # Exemplo: "Exemplo de string"

# Inversão da string
string_invertida = inverter_string(string_original)

# Exibição do resultado
print(f"String original: {string_original}")
print(f"String invertida: {string_invertida}")
