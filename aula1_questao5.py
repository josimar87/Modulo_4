#QUESTAO_5

# Lê a quantidade de respondentes
while True:
    try:
        N = int(input("Digite a quantidade de respondentes: "))
        if N <= 0:
            print("Por favor, digite um número positivo.")
        else:
            break
    except ValueError:
        print("Por favor, digite um número inteiro.")

# Inicializa a soma das idades
soma_idades = 0

# Lê as idades e calcula a soma
for i in range(N):
    while True:
        try:
            idade = int(input(f"Digite a idade do respondente {i+1}: "))
            if idade < 0:
                print("Por favor, digite uma idade válida (não negativa).")
            else:
                break
        except ValueError:
            print("Por favor, digite um número inteiro.")
    soma_idades += idade

# Calcula a média
media = soma_idades / N

# Imprime a média
print(f"A média de idade dos respondentes é: {media:.2f}")
