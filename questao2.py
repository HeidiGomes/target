def is_fibonacci_number(n):
    """
    Verifica se um número pertence à sequência de Fibonacci.
    """
    if n < 0:
        return False

    # Função auxiliar para verificar se x é um quadrado perfeito
    def is_perfect_square(x):
        s = int(x**0.5)
        return s * s == x

    # Um número é de Fibonacci se (5*n^2 + 4) ou (5*n^2 - 4) for um quadrado perfeito
    test1 = 5 * n * n + 4
    test2 = 5 * n * n - 4

    return is_perfect_square(test1) or is_perfect_square(test2)

def fibonacci_sequence_up_to(n):
    """
    Gera a sequência de Fibonacci até o número n (ou próximo maior).
    """
    sequence = []
    a, b = 0, 1
    while a <= n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Escolha como o número será definido:
# Opção 1: Definir o número diretamente no código
# number = 21  # Descomente esta linha e comente a próxima caso queira usar um valor fixo

# Opção 2: Entrada do usuário pelo terminal
number = int(input("Informe um número: "))

# Calcula a sequência de Fibonacci até o número informado
sequence = fibonacci_sequence_up_to(number)

# Verifica se o número pertence à sequência
if is_fibonacci_number(number):
    print(f"O número {number} pertence à sequência de Fibonacci.")
else:
    print(f"O número {number} NÃO pertence à sequência de Fibonacci.")

# Exibe a sequência gerada
print("Sequência de Fibonacci até", number, ":", sequence)
