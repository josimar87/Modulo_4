
def avalia_aluno():
    print("--- Avaliação de Notas ---")

    # Leitura de n1, n2, n3
    while True:
        try:
            n1 = float(input("Digite a primeira nota: "))
            n2 = float(input("Digite a segunda nota: "))
            n3 = float(input("Digite a terceira nota: "))
            break
        except ValueError:
            print("Erro: Por favor, digite valores numéricos válidos para as notas.")

    # Cálculo da média
    m = (n1 + n2 + n3) / 3

    # Exibe a média calculada
    print(f"\nA média (m) calculada é: {m:.2f}")

    # Estrutura Condicional (if/elif/else)
    if m >= 60:
        print("Aprovado")
    elif m >= 40:
        print("Recuperação")
    else:
        print("Reprovado")

    # Imprime "Fim"
    print("\nFim")

# Chama a função
avalia_aluno()
